from django.shortcuts import render, redirect
from .models import Todo
# Create your views here.



def index(request):
    tasks = Todo.objects.all()

    return render(request, 'index.html', {'tasks': tasks})


def add_task(request):
    if request.method == 'POST':
        Title = request.POST['Title']
        Todo.objects.create(Title = Title)

        return redirect('index')
    
def delete_task(request, task_id):
    tasks = Todo.objects.get(pk=task_id)

    tasks.delete()

    return redirect('index')


def mark(request, id):

    tasks = Todo.objects.get(pk = id)

    tasks.completed = True

    tasks.save()

    return redirect('index')
