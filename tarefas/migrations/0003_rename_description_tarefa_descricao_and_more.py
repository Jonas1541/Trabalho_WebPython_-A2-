# Generated by Django 5.1.1 on 2024-09-08 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tarefas', '0002_rename_task_tarefa'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tarefa',
            old_name='description',
            new_name='descricao',
        ),
        migrations.RemoveField(
            model_name='tarefa',
            name='assigned_to',
        ),
        migrations.RemoveField(
            model_name='tarefa',
            name='title',
        ),
        migrations.AddField(
            model_name='tarefa',
            name='titulo',
            field=models.CharField(default='Título Padrão', max_length=200),
        ),
        migrations.AlterField(
            model_name='tarefa',
            name='status',
            field=models.CharField(choices=[('pendente', 'Pendente'), ('andamento', 'Em Andamento'), ('concluida', 'Concluída')], default='pendente', max_length=20),
        ),
    ]
