from ctypes.wintypes import tagSIZE
from importlib.resources import contents
from tabnanny import verbose
from django.utils.text import slugify
from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL
from ckeditor.fields import RichTextField
from cloudinary.models import CloudinaryField

class Tags(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "tags"
    
    def __str__(self):
        return self.title

# Create your models here.
class Posts(models.Model):
    id = models.AutoField(primary_key=True)
    title =  models.CharField(max_length=200)
    desc = models.CharField(max_length=255)
    overview = models.TextField(max_length=300, blank=True, null=True)
    author = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, editable=False, default=None)
    thumbnail = CloudinaryField('image', folder = "saurabhdhakne")
    content =  RichTextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    tags = models.ManyToManyField(Tags, default=None)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            value = self.title
            self.slug = slugify(value, allow_unicode=True)
            # print(f"updating slug value to {self.slug}")
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "posts"
        ordering = ['-created_at']