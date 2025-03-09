from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from Projects.models import Project

@login_required
def home(request):
    latest_projects = Project.objects.all().order_by('-created_at')[:2]
    return render(request, "home.html", {"latest_projects":latest_projects})
