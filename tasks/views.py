from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm
from django.contrib import messages
# Create your views here.

def taskList(request):
    tasks = Task.objects.all().order_by('-created_at')
    return render(request, 'tasks/list.html', {'tasks': tasks})


def taskview(request, id):
    task = get_object_or_404(Task, pk=id)
    return render(request, 'tasks/task.html', {'task': task})


def newtask(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.done = 'doing'
            task.save()

            messages.success(request, 'Tarefa salva com sucesso.')
            
            return redirect('/')

    else:
        form = TaskForm()
        return render(request, 'tasks/newtask.html', {'form': form})

def editTask(request, id):
    task = get_object_or_404(Task, pk=id)
    form = TaskForm(instance=task)

    if(request.method == 'POST'):
        form = TaskForm(request.POST, instance=task)

        if(form.is_valid()):
            task.save()

            messages.success(request,'Mensagem editada com sucesso.')

            return redirect('/')
        else:
            return render(request, 'tasks/edittask.html', {'form': form, 'task': task})
    else:
        return render (request, 'tasks/edittask.html', {'form': form, 'task': task})



def deleteTask(request, id):
    task = get_object_or_404(Task, pk=id)
    task.delete()

    messages.warning(request, 'Tarefa deletada com sucesso.')

    return redirect('/')


def helloword(request):
    return HttpResponse('Olá mundo')


def yourName(request, name):
    return render(request, 'tasks/yourname.html', {'name': name})