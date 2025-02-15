from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Task, Project
from .forms import CreateNewTask, CreateNewProject


# Create your views here.

def hola(request, username):
    print(username)
    return HttpResponse("<h1>Hello %s</h1>" % username)

def index(request):
    title = 'My first Django project'
    return render (request, 'index.html', {'title': title})

def projects(request):
    project_list=list(Project.objects.values())
    return render (request, 'projects/projects.html', {'project_list': project_list})

def tasks(request):
    #t=get_object_or_404(Task, id=id)
    task_list = Task.objects.all()
    return render (request, 'tasks/tasks.html', {'task_list': task_list})

def create_task(request):
    if request.method == 'GET':
        return render(request, 'tasks/create_task.html', {'form': CreateNewTask()})
    else:
        Task.objects.create(
            title=request.POST['title'],
            description=request.POST['description'],
            project_id=1
        )
        return redirect('/tasks/')
    
def create_project(request):
    if request.method == 'GET':
        return render(request, 'projects/create_project.html', {'form': CreateNewProject()})
    else:
        Project.objects.create(name=request.POST['name'])
        return redirect('/projects/')

def project_detail(request, id):
    project = get_object_or_404(Project, id=id)
    task_filtered = Task.objects.filter(project_id=id)
    return render(request, 
                  'projects/project_detail.html', 
                  {'project': project, 'task_filtered': task_filtered})
