from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import HttpResponse
from .models import Tarefa
from .forms import TarefaForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import get_template
from django.template import TemplateDoesNotExist
from django.contrib.auth import login
from .forms import UserRegistrationForm
from django.contrib.auth.models import User

@login_required
def lista_tarefas(request):
    tarefas_pendentes = Tarefa.objects.filter(responsavel=request.user, status='pendente')
    tarefas_andamento = Tarefa.objects.filter(responsavel=request.user, status='andamento')
    tarefas_concluidas = Tarefa.objects.filter(responsavel=request.user, status='concluida')

    context = {
        'tarefas_pendentes': tarefas_pendentes,
        'tarefas_andamento': tarefas_andamento,
        'tarefas_concluidas': tarefas_concluidas,
    }

    return render(request, 'tarefas/lista_tarefas.html', context)

def criar_tarefa(request):
    if request.method == 'POST':
        form = TarefaForm(request.POST, user=request.user)
        if form.is_valid():
            tarefa = form.save(commit=False)
            tarefa.responsavel = form.cleaned_data['responsavel']
            tarefa.save()
            return redirect('lista_tarefas')
    else:
        form = TarefaForm(user=request.user)
    return render(request, 'tarefas/criar_tarefa.html', {'form': form})

def editar_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)
    if request.method == 'POST':
        form = TarefaForm(request.POST, instance=tarefa, user=request.user)
        if form.is_valid():
            tarefa.responsavel = form.cleaned_data['responsavel']
            form.save()
            return redirect('lista_tarefas')
    else:
        form = TarefaForm(instance=tarefa, user=request.user)
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

def debug_logout_template_path(request):
    template_name = 'registration/logged_out.html'
    try:
        template = get_template(template_name)
        return HttpResponse(f'Template found at: {template.origin}')
    except TemplateDoesNotExist:
        return HttpResponse('Template not found')

def custom_logout(request):
    logout(request)
    return render(request, 'registration/logged_out2.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def dashboard(request):
    nome = request.GET.get('nome', '')
    status = request.GET.get('status', '')
    usuario_id = request.GET.get('usuario', '')

    tarefas = Tarefa.objects.all()

    if nome:
        tarefas = tarefas.filter(titulo__icontains=nome)
    if status:
        tarefas = tarefas.filter(status=status)
    if usuario_id:
        tarefas = tarefas.filter(responsavel_id=usuario_id)

    usuarios = User.objects.all()

    num_pendentes = tarefas.filter(status='pendente').count()
    num_andamento = tarefas.filter(status='andamento').count()
    num_concluidas = tarefas.filter(status='concluida').count()

    context = {
        'tarefas': tarefas,
        'usuarios': usuarios,
        'num_pendentes': num_pendentes,
        'num_andamento': num_andamento,
        'num_concluidas': num_concluidas,
        'filtro_nome': nome,
        'filtro_status': status,
        'filtro_usuario': usuario_id
    }

    return render(request, 'dashboard/dashboard.html', context)
