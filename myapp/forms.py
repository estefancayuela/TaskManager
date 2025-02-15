from django import forms
from .models import Project

class CreateNewTask(forms.Form):
    title = forms.CharField(label="Título de tarea", max_length=200)
    description = forms.CharField(widget=forms.Textarea, label="Descripción de la tarea", required=False)

class CreateNewProject(forms.Form):
    name = forms.CharField(label="Nombre del proyecto", max_length=200)