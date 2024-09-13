from django import forms
from .models import Tarefa
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class TarefaForm(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = ['titulo', 'descricao', 'status', 'responsavel']
        widgets = {
            'descricao': forms.Textarea(attrs={'rows': 3}),
            'status': forms.Select(choices=[
                ('pendente', 'Pendente'),
                ('andamento', 'Em Andamento'),
                ('concluida', 'Concluída')
            ]),
            'responsavel': forms.Select(),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['responsavel'].queryset = User.objects.all()
            self.fields['responsavel'].initial = user

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
