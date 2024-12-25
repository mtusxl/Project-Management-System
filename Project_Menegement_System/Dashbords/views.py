from django.shortcuts import render, get_object_or_404
from Projects.models import Project
def home(request):

    projects = Project.objects.all()
    projects_data = []
    for project in projects:
        project_data = {}
        for field in project._meta.get_fields():
           project_data[field.name]= getattr(project, field.name)
        projects_data.append(project_data)
    

    # Передаем данные в шаблон
    context = {'projects_data': projects_data}
    return render(request, "home.html")
