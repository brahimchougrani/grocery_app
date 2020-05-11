from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from phone_field import PhoneField

# Create your models here.

User = get_user_model()


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    street_address = models.CharField(max_length=225, blank=True, null=True)
    city = models.CharField(max_length=225, blank=True, null=True)
    postal_code = models.CharField(max_length=225, blank=True, null=True)
    phone = PhoneField(blank=True, null=True, help_text='Contact phone number')

    def __str__(self):
        return self.user.email


@receiver(post_save, sender=User)
def create_profile(instance, created, *args, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
