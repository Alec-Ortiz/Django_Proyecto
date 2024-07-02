from django import forms
from .models import Tareas

class FormularioTarea(forms.ModelForm):
    class Meta:
        
        model = Tareas
        fields = ['nombreTarea', 'descripcionTarea']