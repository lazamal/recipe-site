from django import forms
from .models import Food

class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['food_name', 'ingredients', 'recepie', 'rating']