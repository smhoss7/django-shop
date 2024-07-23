from django.contrib.auth.models import AbstractUser ,AbstractBaseUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    mobile = models.CharField(max_length=11, null=True, blank=True, unique=True)
    email_active_code = models.CharField(max_length=100)

    def __str__(self):
        return self.get_full_name()


# class User(models.Model):
#     email = models.EmailField(unique=True)
#     name = models.CharField(max_length=100,null=True,blank=True)
#     password = models.CharField(max_length=100)
#     is_active = models.BooleanField(default=True)