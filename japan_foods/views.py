from django.shortcuts import render
from japan_foods.models import Food

# Create your views here.
def index(request):
    japan_foods_queryset = Food.objects.all()
    temp_name = 'japan_foods/index.html'
    context = {
        'foods':japan_foods_queryset

    }
 
    return render(request = request, template_name = temp_name, context = context)
