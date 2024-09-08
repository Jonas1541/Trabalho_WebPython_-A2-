from django.db import models

from django.contrib.auth.models import User

class Tarefa(models.Model):
    titulo = models.CharField(max_length=200, default='Título Padrão')  # Adicione um valor padrão
    descricao = models.TextField()
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('em_andamento', 'Em Andamento'),
        ('concluida', 'Concluída'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente')
    responsavel = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tarefas', default=2)
    
    def __str__(self):
        return self.titulo

class Meta:
    db_table = 'tarefas'  # Define o nome da tabela no banco de dados