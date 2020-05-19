from django.db import models
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone_number = PhoneNumberField(null=False, blank=False, unique=True)
    

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)
