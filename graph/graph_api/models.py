from django.db import models
from django.contrib.auth.models import User

class Graph(models.Model):# Create your models here.

    task = models.CharField(max_length = 180)
    timestamp = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)


    def __str__(self):
        return self.task