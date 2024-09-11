from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Tarefa
from .forms import TarefaForm

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Tarefa

@login_required
def lista_tarefas(request):
    print("VRAUUUUUUUUUUUU: " + str(request.user))
    tarefas_pendentes = Tarefa.objects.filter(responsavel=request.user, status='pendente')
    tarefas_andamento = Tarefa.objects.filter(responsavel=request.user, status='em_andamento')
    tarefas_concluidas = Tarefa.objects.filter(responsavel=request.user, status='concluida')

    context = {
        'tarefas_pendentes': tarefas_pendentes,
        'tarefas_andamento': tarefas_andamento,
        'tarefas_concluidas': tarefas_concluidas,
    }

    return render(request, 'tarefas/lista_tarefas.html', context)

def criar_tarefa(request):
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            tarefa = form.save(commit=False)  # Não salva ainda
            tarefa.responsavel = request.user  # Atribui o usuário logado
            form.save()
            return redirect('lista_tarefas')
    else:
        form = TarefaForm()
    return render(request, 'tarefas/criar_tarefa.html', {'form': form})

def editar_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)
    if request.method == 'POST':
        form = TarefaForm(request.POST, instance=tarefa)
        if form.is_valid():
            form.save()
            return redirect('lista_tarefas')
    else:
        form = TarefaForm(instance=tarefa)
    return render(request, 'tarefas/editar_tarefa.html', {'form': form, 'tarefa': tarefa})

def excluir_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)
    if request.method == 'POST':
        tarefa.delete()
        return redirect('lista_tarefas')
    return render(request, 'tarefas/excluir_tarefa.html', {'tarefa': tarefa})

@csrf_exempt
def atualizar_status_tarefa(request):
    if request.method == 'POST':
        tarefa_id = request.POST.get('tarefa_id')
        novo_status = request.POST.get('status')

        tarefa = Tarefa.objects.get(id=tarefa_id)
        tarefa.status = novo_status
        tarefa.save()

        return JsonResponse({'message': 'Status atualizado com sucesso!'})
    
def index(request):
    return render(request, 'index/index.html')