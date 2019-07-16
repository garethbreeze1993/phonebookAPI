from django.db import models

class PhoneInfo(models.Model):
    first_name = models.CharField(max_length=28)
    last_name = models.CharField(max_length=28)
    relationship = models.CharField(max_length=32)
    mobile_number = models.CharField(max_length=12)
    landline_number = models.CharField(max_length=12, blank=True, null=True)
    owner = models.ForeignKey('auth.User', related_name='numbers', on_delete=models.CASCADE)
