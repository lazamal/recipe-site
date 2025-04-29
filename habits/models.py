from django.db import models
from django.db.models import CharField

# Create your models here.
class Habit(models.Model):
    name = CharField(verbose_name="הרגל", max_length=30, null=False)
    
    