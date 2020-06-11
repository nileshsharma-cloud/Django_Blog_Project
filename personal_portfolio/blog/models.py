from django.db import models

# Create your models here.
<<<<<<< HEAD
=======
class Category(models.Model):
    name = models.CharField(max_length=250)

class Post(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('category', related_name='posts')

    
>>>>>>> 5f22d5296f3920bca31aa761777a51aad2dc39a9
