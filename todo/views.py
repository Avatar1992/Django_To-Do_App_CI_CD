from django.shortcuts import redirect
from .models import Task

def add_task(request):
    if request.method == "POST":
        title = request.POST.get("title")
        if title:
            Task.objects.create(title=title)
    return redirect("index")

