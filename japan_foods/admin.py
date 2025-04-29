from django.contrib import admin
from japan_foods.models import Food

# Register your models here.
@admin.register(Food)
class FoodsAdmin(admin.ModelAdmin):
    list_display = ["id", "food_name",'ingredients', "recepie", "rating"]

    def full_name(self,obj):
        return f"{obj.first_name} {obj.surname}"
