from django.shortcuts import render, redirect

from django.http import HttpResponse

from django.db import models

from django import forms

from .models import Task
# Create your views here.
def index(request):
    #display all the objects 
    tasks = Task.objects.all()
    return render(request,'todoApp/content.html',{'tasks':tasks})


def addForm(request):
    #submit data to the server
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
    
class updateTask(forms.Form):

    #display name instead of the self objects


    name = models.CharField(max_length=100)
    storyPoints = models.PositiveIntegerField()
    action = models.TextField()



class updateTaskForm(forms.ModelForm):
	name= forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Add new task...'}))

	class Meta:
		model = Task
		fields = '__all__'


def edit(request,id):
    task = Task.objects.get(id=id)
    form = updateTaskForm(instance=task)
    
    if request.method == 'POST':
        form = updateTaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}

    return render(request,'todoApp/edit.html', context)







