from django.contrib import admin
from japan_foods.models import Food, Author, Comment

# Register your models here.
@admin.register(Food)
class FoodsAdmin(admin.ModelAdmin):
    list_display = ["id", "food_name",'ingredients', "recepie", "rating", "author", "created_at"]

    
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ["author_name"]

    
@admin.register(Comment)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['food', 'text', 'writer', 'created_at']


