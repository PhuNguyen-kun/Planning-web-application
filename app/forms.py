from django import forms
from .models import Homework

class HomeworkForm(forms.ModelForm):
    class Meta:
        model = Homework
        fields = ['name', 'note', 'due_date', 'difficulty']