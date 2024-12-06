from django import forms
from .models import Report

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['work_type', 'members_count', 'floor_number', 'equipments_used', 'photos', 'report_details']
        widgets = {
            'work_type': forms.TextInput(attrs={'class': 'form-control'}),
            'members_count': forms.NumberInput(attrs={'class': 'form-control'}),
            'floor_number': forms.TextInput(attrs={'class': 'form-control'}),
            'equipments_used': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'photos': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'report_details': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }
