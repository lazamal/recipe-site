
from django.urls import path
from japan_foods import views

app_name = "japan_foods"
urlpatterns = [
    path("",views.index, name="index"),
    path("add_post/",views.add_post,name = "add_post"),
    path('edit/<int:post_id>/', views.edit_post, name="edit_post"),
    path("post/<int:post_id>", views.single_post, name = "single_post")
]