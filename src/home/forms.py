from django import forms
from django.forms.widgets import DateInput
from home.models import Task

class TaskForm(forms.ModelForm):
    class Meta: 
        model = Task
        fields = ['task_name', 'description', 'due_date']
        labels = {
            'task_name': '',
            'description': '',
            'due_date': ''
        }

        widgets = {
            'due_date': DateInput(attrs={'type': 'date', 'class': 'due-date-class', 'placeholder': 'Due Date'}),
        }

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)

        self.fields['task_name'].widget.attrs.update({'class': 'task-name-class', 'placeholder': 'Task Name'})
        self.fields['description'].widget.attrs.update({'class': 'description-class', 'placeholder': 'Description'})