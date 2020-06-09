from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=250)

class Post(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('category', related_name='posts')

    