
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from SndMessage.msg import process  

class StoreData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='store_data')
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    msg = models.TextField()

    def __str__(self):
        return self.name

# Signal to send email after StoreData instance is created
@receiver(post_save, sender=StoreData)
def send_email_on_creation(sender, instance, created, **kwargs):
    if created:
        # Call the process function to send an email
        process(instance)
