from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('projects/', views.projects, name='all_projects'),
    path('projects/<int:id>', views.project_detail, name='project_details'),
    path('create_project/', views.create_project, name='create_project'),
    path('tasks/', views.tasks, name='all_tasks'),
    path('create_task/<int:id>', views.create_task, name='create_task'),
    path('delete_project/<int:id>/', views.delete_project, name='delete_project'),
    path('delete_task/<int:id>/', views.delete_task, name='delete_task'),
]
