from django import forms
from .models import Todo

class CreateTodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'info', 'remind_at']


class UpdateTodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'info', 'remind_at']
