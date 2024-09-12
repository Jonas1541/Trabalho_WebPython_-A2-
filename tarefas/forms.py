from django import forms
from .models import Tarefa
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
class TarefaForm(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = ['titulo', 'descricao', 'status']
        widgets = {
            'descricao': forms.Textarea(attrs={'rows': 3}),
            'status': forms.Select(choices=[
                ('pendente', 'Pendente'),
                ('em_andamento', 'Em Andamento'),
                ('concluida', 'Concluída')
            ])
        }
class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
