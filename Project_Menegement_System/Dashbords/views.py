from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from Projects.models import Project

@login_required
def home(request):
    return render(request, "home.html")
