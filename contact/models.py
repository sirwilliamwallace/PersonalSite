from django.db import models


# Create your models here.
class ContactModel(models.Model):
    title = models.CharField(max_length=300, verbose_name='Title')
    email = models.EmailField(verbose_name='Email Address')
    full_name = models.CharField(max_length=100, verbose_name='Full Name')
    message = models.TextField(verbose_name='Message from Client')
    response = models.TextField(verbose_name='Response from Admin', null=True, blank=True)
    createDate = models.DateTimeField(auto_now_add=True, verbose_name='Created date')
    isRead = models.BooleanField(default=False, verbose_name='Is the message read by the Admin')

    def __str__(self):
        return f"{self.full_name} - {self.email}"

    class Meta:
        verbose_name = 'Contact Module'
        verbose_name_plural = "Contact Form's"
