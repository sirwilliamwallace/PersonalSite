from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    phone_number = models.CharField(max_length=100, blank=True, null=True, verbose_name='Phone Number')
    email_verification_code = models.CharField(max_length=100, verbose_name='Email Verification Code')

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.get_full_name()