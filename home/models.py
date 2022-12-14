from user_accounts.models import User
from django.db import models


class Hero(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Name')
    skills = models.ManyToManyField('Skills', verbose_name='Skills')
    bg_image = models.ImageField(verbose_name='Background Image', upload_to='back_ground_image/')

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Hero Section'
        verbose_name_plural = 'Hero Section'


class Skills(models.Model):
    skill = models.CharField(max_length=50)
    short_description = models.CharField(max_length=300, null=True)

    def __str__(self):
        return f"{self.skill}"

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills Section'


class SiteSettings(models.Model):
    logo = models.ImageField()

    class Meta:
        verbose_name = 'Settings'
        verbose_name_plural = 'Settings'

    def __str__(self):
        return f"Logo number {self.id}"


class IpLog(models.Model):
    visits_count = models.IntegerField(default=0, verbose_name="Count of Visitors")
    ip_address = models.CharField(max_length=25, verbose_name="Visitor's Ip Address ")
    authenticated_user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, verbose_name="User ")

    def __str__(self):
        return self.ip_address

    class Meta:
        verbose_name = "Logged ip"
        verbose_name_plural = "Logged IP's"


class Profile(models.Model):
    avatar = models.ImageField(verbose_name='Avatar ')
    name = models.CharField(max_length=100, verbose_name='Name ')
    profile = models.CharField(max_length=100, verbose_name='Skills ')
    email = models.EmailField(max_length=300, verbose_name='Email Address ')
    phone = models.CharField(max_length=100, verbose_name='Phone Number')
    about = models.TextField(verbose_name='About ', null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = "Profile's"


class SocialMediaAccounts(models.Model):
    platform = models.CharField(max_length=50, verbose_name="Social media platform")
    account_link = models.URLField(max_length=200, verbose_name="Account reference link")

    def __str__(self):
        return self.platform

    class Meta:
        verbose_name = "Social Media Account"
        verbose_name_plural = "Social Media Account's"


class GetInTouch(models.Model):
    getInTouchText = models.TextField(verbose_name="Get in touch text")
    address = models.CharField(max_length=300, verbose_name="Address ", null=True, blank=True)
    phone_number = models.CharField(
        max_length=150, verbose_name="Phone Number", null=True, blank=True)
    email_address = models.EmailField(
        verbose_name="Email Address ", null=True, blank=True)
    social_media = models.ManyToManyField(SocialMediaAccounts, verbose_name="Social media accounts", blank=True,
                                          related_name='platforms')
    isActive = models.BooleanField(default=False, verbose_name="Be shown in contact section")

    class Meta:
        verbose_name = "Get in touch"
        verbose_name_plural = "Get in touch module"

    def __str__(self):
        return f"{self.id} - {self.phone_number} - {self.email_address}"


class Keywords(models.Model):
    keyword = models.CharField(max_length=20, verbose_name="Keywords Meta Tag")

    def __str__(self):
        return self.keyword

    class Meta:
        verbose_name = "Keyword"
        verbose_name_plural = "Keywords"


class Seo(models.Model):
    keywords_connection = models.ManyToManyField('Keywords', verbose_name='Keywords', related_name='keywords_for_seo')
    description = models.TextField(verbose_name="Description Meta Tag")
    isMain = models.BooleanField(default=False, verbose_name="Main Meta Tags for Site")

    def __str__(self):
        return f"Seo settings number {self.id}"

    class Meta:
        verbose_name = "Meta tag"
        verbose_name_plural = "Seo Meta tags"
