from django.contrib import admin
from .models import Author, Post


# Register your models here.
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ["id", "full_name", "email", "phone"]

    def full_name(self,obj):
        return f"{obj.first_name} {obj.surname}"

