from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Food(models.Model):
    def __str__(self):
           return f'{self.food_name}'
    food_name = models.CharField(verbose_name="שם האוכל", max_length=30, null=False)
    ingredients = models.CharField(verbose_name="מצרכים", max_length=30, null=False)
    recepie = models.TextField(verbose_name="מתכון", max_length=500, null=True, blank=True)
    rating = models.IntegerField(verbose_name="דירוג", validators=[MinValueValidator(1), MaxValueValidator(5)], null=True, blank=True)
   