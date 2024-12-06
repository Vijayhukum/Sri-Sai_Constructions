from django.db import models

from cloudinary.models import CloudinaryField






class Site(models.Model):
    sitename = models.CharField(max_length=255, unique=True)  
    address = models.TextField() 
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.sitename



class Report(models.Model):
    site = models.ForeignKey(Site, on_delete=models.CASCADE, related_name='reports')
    work_type = models.CharField(
        max_length=150
    )
    members_count = models.BigIntegerField(
    )
    floor_number = models.CharField(
        max_length=50
    )
    equipments_used = models.TextField()
    photos = CloudinaryField('reports-photos', blank=True, null=True)
    report_details = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Report: {self.work_type} on Floor {self.floor_number} at {self.site}"

    class Meta:
        ordering = ['-created_at']


    def save(self, *args, **kwargs):
        # Log the file URL
        super().save(*args, **kwargs)    
        if self.photos:
            print(f"Uploaded photo URL: {self.photos.url}")  