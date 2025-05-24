from django.contrib import admin
from japan_foods.models import Food, Author

# Register your models here.
@admin.register(Food)
class FoodsAdmin(admin.ModelAdmin):
    list_display = ["id", "food_name",'ingredients', "recepie", "rating", "author", "created_at"]

    def full_name(self,obj):
        return f"{obj.first_name} {obj.surname}"
    
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ["author_name"]

    def full_name(self,obj):
        return f"{obj.author_name}"
