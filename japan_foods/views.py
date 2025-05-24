from datetime import datetime
from django.shortcuts import render, redirect
from japan_foods.models import Food, Author
from .forms import FoodForm
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
        

def index(request):
    
    query = request.GET.get('q')
    
    food_checked = request.GET.get("food_name", None)
    ingredients_checked = request.GET.get('ingredients',None)
    recepie_checked = request.GET.get('recepie',None)
    rating_selected = request.GET.get('rating',None)
    
    temp_name = 'japan_foods/index.html'
    results = Food.objects.all()
    # results.recepie = re.sub(r'\n{2,}', '\n', results.recepie)
    filters = Q()


    if query:
      
        if food_checked:
           filters |= Q(food_name__icontains=query)
        if ingredients_checked:
           filters |= Q(ingredients__icontains=query)
        if recepie_checked:
            filters |= Q(recepie__icontains=query)
      
  

        # if no checkboxes are checked
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
        'menu':results,
        'query':query,
    }
    
    return render(request, temp_name, context= context)


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
    

# class SearchResultsView(ListView):
#     model = Food
#     template_name = 'japan_foods/search_results.html'
#     context_object_name = 'foods'

#     def get_queryset(self):
#         query = self.request.GET.get('q')
        
#         return Food.objects.filter(food_name__icontains=query)


   



