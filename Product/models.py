import enum

from django.db import models
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.

class Brand(models.Model):
    name = models.CharField(max_length=100,verbose_name='brand name')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='slug')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Brand,self).save(*args, **kwargs)

    def __str__(self):
        return self.name



class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)


class Gender(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Gender, self).save(*args, **kwargs)


class Color(models.TextChoices):
    BLUE = 'blue'
    GREEN = 'green'
    RED = 'red'


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    discount = models.IntegerField()
    stock = models.IntegerField()
    description = models.TextField()
    color = models.CharField(max_length=10, choices=Color.choices, default=Color.BLUE)
    is_published = models.BooleanField(default=False)
    rating = models.IntegerField()  # visit validator in python
    slug = models.SlugField(db_index=True)
    category = models.ManyToManyField(Category, related_name='products')
    gender = models.ManyToManyField(Gender, related_name='products')
    brand = models.ManyToManyField(Brand, related_name='products',blank=True)
    image=models.ImageField(upload_to='products/',null=True,blank=True)
    #category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    #gender = models.ForeignKey(Gender, on_delete=models.CASCADE, default=1)

    class Meta:
        verbose_name = 'محصولات'

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.slug])

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.slug = slugify(str(self.name) + ' ' + str(self.id))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
