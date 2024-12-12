from django.shortcuts import render

def all_tasks(request):
    return render(request, "my_tasks.html")
