from django.contrib.auth import views as auth_views
from django.urls import path
from .views import home,add_site,report_detail,today_reports,all_sites,site_detail,add_report,edit_report,login_view,base

urlpatterns = [
    path('', base, name='base'),
    path('home/',home,name='home'),
    path('add-site/', add_site, name='add_site'),
    path('site/<int:site_id>/add-report/', add_report, name='add_report'),
    path('edit-report/<int:pk>/', edit_report, name='edit-report'),

    path('today-reports/', today_reports, name='today_reports'),
    path('report/<int:report_id>/',report_detail, name='report_detail'),


    path('all-sites/', all_sites, name='all_sites'),  # All sites
    path('site/<int:site_id>/', site_detail, name='site_detail'), 

    path('login/', login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]