from django.db import models

# Create your models here.
class Black(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    slug =  models.CharField(max_length=130)
    timestamp = models.DateTimeField(blank=True)

    def __str__(self):
        return self.title

class White(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    slug = models.CharField(max_length=135)
    timestamp = models.DateTimeField(blank=True)

    def __str__(self):
        return self.title