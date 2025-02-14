from django import forms

class CreateNewTask(forms.Form):
    title = forms.CharField(label="Título de tarea", max_length=200)
    description = forms.CharField(widget=forms.Textarea, label="Descripción de la tarea", required=False)