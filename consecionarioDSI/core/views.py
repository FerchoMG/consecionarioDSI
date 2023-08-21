from django.shortcuts import render, HttpResponse, redirect
from .models import Project
from .models import info

# Create your views here.
def home(request):
    projects = Project.objects.all()

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        info.objects.create(name=name, email=email, message=message)
        return redirect('home')  # Redirigir a la misma página después de enviar

    return render(request, "core/base.html", {'projects' : projects})
