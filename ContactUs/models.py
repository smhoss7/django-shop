from django.db import models
from django.utils.text import slugify


# Create your models here.


class Contact(models.Model):
    title = models.CharField(max_length=300)
    email = models.EmailField(max_length=300)
    message = models.TextField()
    full_name = models.CharField(max_length=300)
    is_read = models.BooleanField(default=False)
    start_date = models.DateField(auto_now_add=True)
    answer=models.TextField(null=True,blank=True)
    slug = models.SlugField(max_length=300,unique=True)

    def save(self, *args, **kwargs):
        super(Contact, self).save(*args, **kwargs)
        self.slug=slugify(str(self.title)+" "+str(self.id))
        super(Contact, self).save(*args, **kwargs)



class SendClass(models.Model):
    image=models.ImageField(upload_to='temp')
