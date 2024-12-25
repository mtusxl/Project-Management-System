from django.shortcuts import render


def Create_project(request):
    return  render(request, 'project_form.html')
