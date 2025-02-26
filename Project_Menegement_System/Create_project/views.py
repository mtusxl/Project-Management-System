from django.shortcuts import render
from Projects.models import Project
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from Users.models import User

@login_required
def Create_project(request):
    if request.method=="POST":
        User = get_user_model()
        
        name=request.POST.get("project_name")
        description = request.POST.get("project_description")
        members = request.POST.getlist("members")
        
        project = Project(
            name = name,
            description = description,
            author=request.user
        )
        project.save()
        members = User.objects.filter(id__in=members)
        project.members.set(members)
        request.user.projects.add(project)
        
   
    return  render(request, 'project_form.html')
