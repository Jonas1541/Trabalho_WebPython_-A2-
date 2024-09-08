from django import forms
from .models import Tarefa

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
