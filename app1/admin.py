from django.contrib import admin
from .models import Site,Report

class SiteAdmin(admin.ModelAdmin):
    list_display = ('sitename', 'address', 'created_at', 'updated_at')


from django import forms
from .models import Report

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = '__all__'

    photos = forms.ImageField(label='Photo', required=False)

class ReportAdmin(admin.ModelAdmin):
    form = ReportForm
    list_display = ('site', 'work_type', 'members_count', 'floor_number', 'created_at', 'updated_at')
    list_filter = ('work_type', 'created_at')
    search_fields = ('work_type', 'floor_number', 'equipments_used')
    readonly_fields = ('created_at', 'updated_at')

admin.site.register(Report, ReportAdmin)

admin.site.register(Site, SiteAdmin)
