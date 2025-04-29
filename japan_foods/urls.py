
from django.urls import path
from japan_foods import views

app_name = "japan_foods"
urlpatterns = [
    path("",views.index, name="index")
]
