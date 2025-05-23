from django.urls import path
from blog import views


app_name = "blog"

urlpatterns = [
    path('', views.index, name="index"),
    path('post/<int:post_id>/', views.single_post, name="single_post"),
    path('add_post/', views.add_post, name="add_post"),
    path('edit_post/<int:post_id>/', views.edit_post, name="edit_post")
]