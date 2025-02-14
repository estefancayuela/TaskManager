from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task, Project
from .forms import CreateNewTask


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

def create_task(request):
    if request.method == 'GET':
        return render(request, 'create_task.html', {'form': CreateNewTask()})
    else:
        Task.objects.create(
            title=request.POST['title'],
            description=request.POST['description'],
            project_id=1
        )
        return redirect('/tasks/')