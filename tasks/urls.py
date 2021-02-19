from django.urls import path

from . import views

app_name = "tasks"      #to avoid collison of names such as "index" 

urlpatterns = [
    path("", views.index, name="index"),
    path("add", views.add, name="add")
]