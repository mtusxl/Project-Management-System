from django.shortcuts import render,  redirect
from django.http import HttpResponse



def landing(request):
    if request.user.is_authenticated:
        return redirect("home")
   
    return render(request, "Landing.html")
