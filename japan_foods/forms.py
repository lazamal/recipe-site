from django import forms
from .models import Food, Comment

class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['food_name', 'ingredients', 'recepie', 'rating']

class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text', 'writer']