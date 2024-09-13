from django.db import models

# Create your models here.
from django.core.exceptions import ValidationError

class Setting(models.Model):
    host = models.CharField(max_length=255)
    port = models.IntegerField()
    email = models.EmailField()
    password = models.CharField(max_length=255)
    status = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.pk and Setting.objects.exists():
            raise ValidationError('There can be only one instance of Settings.')
        super(Setting, self).save(*args, **kwargs)

    def __str__(self):
        return self.email
    
class ToEmail(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phonenumber = models.CharField(max_length=15)
    position = models.CharField(max_length=100)
    active_status = models.BooleanField(default=False)

    def __str__(self):
        return self.name