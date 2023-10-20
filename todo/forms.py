from django import forms
from. models import *

class Todo_form(forms.ModelForm):
    models=Todolist
    fields='__all__'