from django.shortcuts import render, redirect

from django.http import HttpResponse 

from .models import Task
# Create your views here.
def index(request):
    #display all the objects 
    tasks = Task.objects.all()
    return render(request,'todoApp/content.html',{'tasks':tasks})


def addForm(request):
    if request.method == "POST":
        #gets the name of the form on the actual request 
        name = request.POST.get("name")
        storyPoints = request.POST.get("storyPoints")
        action = request.POST.get("action")
        task = Task(name=name,storyPoints=storyPoints,action=action)
        task.save()
        return redirect("/")

    return render(request,'todoApp/add.html')

#The task gets removed when the used clicks the button Done
def delete(request,id):

    #get the id of the parameter been passed in
    task = Task.objects.get(id=id)
    if request.method == "POST":
        task.delete()
        return redirect('/')
    return render(request,'todoApp/delete.html')
    










