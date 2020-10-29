from django.shortcuts import render, redirect
from .models import dojos, ninjas

def index(request):
  context = {
    "all_dojos": dojos.objects.all()
  }
  return render(request, "index.html", context)

def process_dojo(request):
  dojos.objects.create(
    name=request.POST['name'],
    city=request.POST['city'],
    state=request.POST['state'],
  )
  return redirect('/')

def process_ninja(request):
  ninjas.objects.create(
    first_name=request.POST['first_name'],
    last_name=request.POST['last_name'],
    dojo_id=request.POST['dojo']
  )
  return redirect('/')