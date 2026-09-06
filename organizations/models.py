from django.db import models

# Create your models here.


class Organization(models.Model):
    name = models.CharField(max_length=150)
    logo = models.ImageField(upload_to="organization_logos/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name 