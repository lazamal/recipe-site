from datetime import datetime
from django.shortcuts import render, redirect
from japan_foods.models import Food, Author
from .forms import FoodForm, CommentsForm
from django.views.generic import TemplateView, ListView
from django.db.models import Q
import re



# Create your views here.

def get_author_for_user(user):
    response, created = Author.objects.get_or_create(author_name=user)
    return response
 

def add_post(request):
    if request.method == "GET":
        temp_name = 'japan_foods/add_post.html'
        return render(request = request, template_name= temp_name)
    
    elif request.method == "POST":
        form = FoodForm(request.POST)
        if form.is_valid():
            food = form.save(commit=False)  
            food.author = get_author_for_user(request.user)  
            food.save() 
            return redirect('japan_foods:index')
        else:
            print(form.errors)  
            return render(request, 'japan_foods/add_post.html', {'form': form})
        

from django.shortcuts import get_object_or_404

def index(request):
    temp_name = 'japan_foods/index.html'
    results = Food.objects.all()
    context = {
        'foods': results
    }

    if request.method == "GET":
        query = request.GET.get('q')
        food_checked = request.GET.get("food_name", None)
        ingredients_checked = request.GET.get('ingredients', None)
        recepie_checked = request.GET.get('recepie', None)
        rating_selected = request.GET.get('rating', None)

        filters = Q()

        if query:
            if food_checked:
                filters |= Q(food_name__icontains=query)
            if ingredients_checked:
                filters |= Q(ingredients__icontains=query)
            if recepie_checked:
                filters |= Q(recepie__icontains=query)

            # If no checkboxes are checked
            if not (food_checked or ingredients_checked or recepie_checked):
                filters = (
                    Q(food_name__icontains=query) |
                    Q(ingredients__icontains=query) |
                    Q(recepie__icontains=query)
                )
        
        if rating_selected:
            filters &= Q(rating__exact=rating_selected)

        results = Food.objects.filter(filters)
        context = {
            'foods': results,
            'query': query,
        }
        return render(request, temp_name, context=context)

    elif request.method == "POST":
        form_type = request.POST.get("comment_form")
        if form_type == 'comment_form':
            form = CommentsForm(request.POST)
            if form.is_valid():
                food_id = request.POST.get('food_id')
                food_instance = get_object_or_404(Food, id=food_id)
                comment = form.save(commit=False)
                comment.food = food_instance
                print('recieved')
                comment.save()
                form = CommentsForm() 
                return redirect(request.path)
            else:
                print(form.errors)
            # Update context with refreshed foods and form
            context["form"] = form
            context["foods"] = Food.objects.all()
    
        return render(request, temp_name, context=context)



def edit_post(request, post_id): 

    post = Food.objects.get(id=post_id)
    print("Editing post:", post.id)

    if request.method == "POST":
        form = FoodForm(request.POST, instance=post)
        print("post:", form)
        if form.is_valid():
            form.save() 
            return redirect('japan_foods:index')
        else:
            print(form.errors)  
            return render(request, 'japan_foods/edit_post.html', {'form': form})
    
   
    temp_name = 'japan_foods/edit_post.html'
    context = {
       'post_id': post_id,
       'post' : post
   }
    
    return render(request, temp_name, context= context)
    


def single_post(request, post_id):
        post = Food.objects.get(id=post_id)

        context = {
                'post': post,
                'food': request
        }

        if request.method == "GET":
            print('got request')
            temp_name = 'japan_foods/single_post.html'
       
            return render(request = request, template_name= temp_name, context=context)
    


   



