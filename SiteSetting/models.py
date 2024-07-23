from django.db import models

# Create your models here.

class SiteSettings(models.Model):
    site_name = models.CharField(max_length=100)
    site_address = models.CharField(max_length=100)
    about_us = models.TextField()
    is_active = models.BooleanField(default=False)
    phone=models.CharField(max_length=100,null=True,blank=True)
    email=models.CharField(max_length=100,null=True,blank=True)
    copyright=models.CharField(max_length=100)
    logo=models.ImageField(upload_to='setting')

    def __str__(self):
        return self.site_name




class FooterTitleLink(models.Model):
    title=models.CharField(max_length=200)
    def __str__(self):
        return self.title


class FooterLinks(models.Model):
    title=models.CharField(max_length=200)
    url=models.URLField(max_length=500)
    footer=models.ForeignKey(FooterTitleLink,on_delete=models.CASCADE)
    def __str__(self):
        return self.title
