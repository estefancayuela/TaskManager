from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('hello/<str:username>', views.hola),
    path('projects/', views.projects),
    path('projects/<int:id>', views.project_detail),
    path('create_project/', views.create_project),
    path('tasks/', views.tasks),
    path('create_task/', views.create_task),
]
