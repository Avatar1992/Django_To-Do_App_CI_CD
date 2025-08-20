from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm

def index(request):
    tasks = Task.objects.all()
    form = TaskForm()
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    return render(request, "todo/index.html", {"tasks": tasks, "form": form})

def delete_task(request, pk):
    task = get_object_or_404(Task, id=pk)
    task.delete()
    return redirect("index")

def toggle_task(request, pk):
    task = get_object_or_404(Task, id=pk)
    task.completed = not task.completed
    task.save()
    return redirect("index")

