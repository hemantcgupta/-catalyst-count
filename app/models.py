from django.db import models

class CompanyData(models.Model):
    name = models.CharField(max_length=255)
    domain = models.URLField(blank=True, null=True)
    year_founded = models.PositiveIntegerField(blank=True, null=True)
    industry = models.CharField(max_length=255, blank=True, null=True)
    size_range = models.CharField(max_length=255, blank=True, null=True)
    locality = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)
    current_employee_estimate = models.PositiveIntegerField(blank=True, null=True)
    total_employee_estimate = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return self.name
