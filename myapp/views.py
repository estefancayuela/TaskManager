from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Task, Project


# Create your views here.

def hola(request, username):
    print(username)
    return HttpResponse("<h1>Hello %s</h1>" % username)

def index(request):
    title = 'My first Django project'
    return render (request, 'index.html', {'title': title})

def projects(request):
    project_list=list(Project.objects.values())
    return render (request, 'projects.html', {'project_list': project_list})

def tasks(request):
    #t=get_object_or_404(Task, id=id)
    task_list = Task.objects.all()
    return render (request, 'tasks.html', {'task_list': task_list})