from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Author(models.Model):
      def __str__(self):
            return f'{self.author_name}'
      author_name = models.ForeignKey(User, on_delete=models.CASCADE, null = True, unique=True)

class Food(models.Model):
    def __str__(self):
          return f'{self.food_name}'
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name="הכותב", null = True)
    food_name = models.CharField(verbose_name="שם האוכל", max_length=30, null=False)
    ingredients = models.TextField(verbose_name="מצרכים", max_length=1000, null=False)
    recepie = models.TextField(verbose_name="מתכון", max_length=1000, null=True, blank=True)
    rating = models.IntegerField(verbose_name="דירוג", validators=[MinValueValidator(1), MaxValueValidator(5)], null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

   