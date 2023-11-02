from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class TodoModel(models.Model):
    title=models.CharField(max_length=100)
    desc=models.CharField(max_length=500)
    file=models.ImageField(upload_to='todo_images',null=True)
    date=models.DateField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)