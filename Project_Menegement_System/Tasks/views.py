from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def all_tasks(request):
    return render(request, "my_tasks.html")
