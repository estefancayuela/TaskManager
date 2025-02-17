from django.shortcuts import render, redirect, get_object_or_404
from .models import Task, Project
from .forms import CreateNewTask, CreateNewProject

# Create your views here.

#Home
def index(request):
    title = 'My first Django project'
    return render (request, 'index.html', {'title': title})


#PROJECTS
def projects(request):
    project_list=list(Project.objects.values())
    return render (request, 'projects/projects.html', {'project_list': project_list})

def create_project(request):
    if request.method == 'GET':
        return render(request, 'projects/create_project.html', {'form': CreateNewProject()})
    elif request.method == 'POST':
        Project.objects.create(name=request.POST['name'])
        return redirect('/projects/')
    
def project_detail(request, id):
    if request.method == 'GET':    
        project = get_object_or_404(Project, id=id)
        task_filtered = Task.objects.filter(project_id=id, done=False)
        task_done = Task.objects.filter(project_id=id, done=True)
        return render(request, 
                    'projects/project_detail.html', 
                    {'project': project, 'task_filtered': task_filtered, 'task_done': task_done})
    else:
        return redirect('/create_task/%s' % id)


def delete_project(request, id):
    projectToDelete = get_object_or_404(Project, id=id)
    projectToDelete.delete()
    return redirect('/projects/')


#TASKS
def create_task(request, id):
    if request.method == 'GET':
        return render(request, 
                      'tasks/create_task.html', 
                      {'form': CreateNewTask()})
    elif request.method == 'POST':
        Task.objects.create(
            title=request.POST['title'],
            description=request.POST['description'],
            project_id=id,)
        return redirect('/projects/%s' % id)

def done_task(request, id):
    task = get_object_or_404(Task, id=id)
    if task.done == True:
        task.done = False
    else:
        task.done = True
    task.save()
    return redirect('/projects/%s' % task.project_id)

def delete_task(request, id):
    task_projectID = Task.objects.get(id=id).project_id
    TaskToDelete = get_object_or_404(Task, id=id)
    TaskToDelete.delete()
    return redirect('/projects/%s' % task_projectID)

def delete_done_tasks(request, id):
    Task.objects.filter(project_id=id, done=True).delete()
    return redirect('/projects/%s' % id)
