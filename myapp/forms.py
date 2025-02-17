from django import forms
from .models import Project

class CreateNewTask(forms.Form):
    title = forms.CharField(label="Task title", max_length=200)
    description = forms.CharField(widget=forms.Textarea, label="Task description", required=False)

class CreateNewProject(forms.Form):
    name = forms.CharField(label="Nombre del proyecto", max_length=200)