from django.db import models

# Create your models here.
class Author(models.Model):
    def __str__(self):
        return f"{self.first_name} {self.surname}"
    first_name = models.CharField(verbose_name="שם",max_length=255)
    surname = models.CharField(verbose_name="משפחה",max_length=255)
    email = models.EmailField(verbose_name = "דואר אלקטרוני", null = True, max_length=255)
    phone = models.CharField(verbose_name="טלפון", null=True, blank = True, max_length=250)


class Post(models.Model):
    def __str__(self):
        return f"{self.title} מאת {self.author}"
    title = models.CharField(verbose_name="כותרת",max_length=255)
    content = models.TextField(verbose_name="תוכן")
    updated_at = models.DateTimeField(verbose_name="עדכון אחרון")
    author = models.ForeignKey(to=Author, on_delete=models.CASCADE)

