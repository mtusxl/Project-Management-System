from django.shortcuts import render

def project_list(request):
    return render(request, "project.html")
