from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm
# Create your views here.

def taskList(request):
    tasks = Task.objects.all().order_by('-created_at')
    return render(request, 'tasks/list.html', {'tasks': tasks})


def taskview(request, id):
    task = get_object_or_404(Task, pk=id)
    return render(request, 'tasks/task.html', {'task': task})


def newtask(request):
    if request.method == 'POST':
        pass
    else:
        form = TaskForm()
        return render(request, 'tasks/newtask.html', {'form': form})



def helloword(request):
    return HttpResponse('Olá mundo')


def yourName(request, name):
    return render(request, 'tasks/yourname.html', {'name': name})