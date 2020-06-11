from django.db import models

# Create your models here.

#Used to create tables in database and variables describe name of te column in database.

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=50)
    image = models.FilePathField(path='/img')