from django.shortcuts import render, redirect
from japan_foods.models import Food
from .forms import FoodForm
from django.views.generic import TemplateView, ListView

# Create your views here.

 

def add_post(request):
    if request.method == "GET":
        temp_name = 'japan_foods/add_post.html'
        return render(request = request, template_name= temp_name)
    elif request.method == "POST":
        form = FoodForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('japan_foods:index')
        return redirect('japan_foods:index') 
    

def search_food(request):
    query = request.GET.get('q')
    temp_name = 'japan_foods/index.html'
    results = Food.objects.all()
    
    if query:
        results = Food.objects.filter(food_name__icontains=query)
    
    context = {
        'menu':results,
        'query':query,
    }

    return render(request, temp_name, context= context)

# class SearchResultsView(ListView):
#     model = Food
#     template_name = 'search_results.html'
#     context_object_name = 'foods'

#     def get_queryset(self):
#         query = self.request.GET.get('q')
        
#         return Food.objects.filter(food_name__icontains=query)


   



