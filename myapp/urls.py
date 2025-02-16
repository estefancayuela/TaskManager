from django.urls import path
from . import views

urlpatterns = [
    #Home
    path('', views.index, name='home'),
    #PROJECTS
    path('projects/', views.projects, name='all_projects'),
    path('projects/<int:id>', views.project_detail, name='project_details'),
    path('create_project/', views.create_project, name='create_project'),
    path('delete_project/<int:id>', views.delete_project, name='delete_project'),
    #TASKS
    path('create_task/<int:id>', views.create_task, name='create_task'),
    path('done_task/<int:id>', views.done_task, name='done_task'),
    path('delete_task/<int:id>', views.delete_task, name='delete_task'),
    path('delete_done_tasks/<int:id>', views.delete_done_tasks, name='delete_done_tasks'),
]
