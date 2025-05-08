
from django.urls import path
from japan_foods import views

app_name = "japan_foods"
urlpatterns = [
    path("",views.index, name="index"),
    path("add_post/",views.add_post,name = "add_post"),
    # path("search_results", views.SearchResultsView.as_view(), name = "search_results")
]