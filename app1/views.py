from django.shortcuts import render, redirect,get_object_or_404
from .models import Site,Report
from .forms import ReportForm
from django.contrib.auth import authenticate, login

from django.contrib import messages
from django.http import HttpResponse
from django.utils import timezone
from django.db.models import DateField
from django.db.models.functions import TruncDate
from collections import defaultdict
from django.contrib.auth.decorators import login_required




def home(request):
    sites = Site.objects.all()

    return render(request, 'home.html', {'sites': sites})


@login_required(login_url='login')
def add_site(request):
    if request.method == "POST":
        sitename = request.POST.get('sitename')
        address = request.POST.get('address')
        print(address,sitename)
        Site.objects.create(sitename=sitename, address=address)

        return redirect('/')  

    return render(request, 'addSite.html')



def add_report(request, site_id):
    site = get_object_or_404(Site, id=site_id)

    if request.method == "POST":
        form = ReportForm(request.POST, request.FILES)
        if form.is_valid():
            report = form.save(commit=False)
            report.site = site
            report.save()
            return redirect('today_reports')  # Redirect to today's reports after saving
    else:
        form = ReportForm()

    return render(request, 'add_report.html', {'form': form, 'site': site})



def edit_report(request, pk):
    report = get_object_or_404(Report, pk=pk)
    if request.method == "POST":
        form = ReportForm(request.POST, request.FILES, instance=report)
        if form.is_valid():
            form.save()
            return redirect('today_reports')  
    else:
        form = ReportForm(instance=report)
    return render(request, 'edit_report.html', {'form': form, 'report': report})



def today_reports(request):
    today = timezone.now().date()

    sites = Site.objects.all()

    
    reports_for_sites = {}
    for site in sites:
        reports_for_sites[site] = Report.objects.filter(site=site, created_at__date=today)

    return render(request, 'today_reports.html', {'reports_for_sites': reports_for_sites, 'today_date': today})


def report_detail(request, report_id):
    report = get_object_or_404(Report, id=report_id)
    return render(request, 'report_detail.html', {'report': report})



def all_sites(request):
    all_sites = Site.objects.all() 
    return render(request, 'allsites.html', {'sites': all_sites})

def site_detail(request, site_id):
    site = get_object_or_404(Site, id=site_id)
    # Fetch reports for the site and group them by date
    reports = Report.objects.filter(site=site).annotate(date=TruncDate('created_at')).order_by('-date')

    reports_by_date = defaultdict(list)
    for report in reports:
        reports_by_date[report.date].append(report)

    return render(
        request,
        'sitedetailfullreport.html',
        {'site_name': site.sitename, 'reports_by_date': dict(reports_by_date)}
    )








def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # If the user is authenticated, log them in
            login(request, user)
            # messages.success(request, 'Login successful!')
            return redirect('home')  # Redirect to homepage after login
        else:
            # If authentication fails, show an error message
            messages.error(request, 'Invalid username or password')
    
    return render(request, 'login.html')