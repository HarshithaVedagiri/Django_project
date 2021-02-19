from django import forms
from django.shortcuts import render
from django.http import HttpResponseRedirect    # for redirecting to the page
from django.urls import reverse

# Create your views here.
# from django.http import HttpResponse

# tasks = []    instead of creating a global variable use "sessons" in django

class NewTaskForm(forms.Form):
    task = forms.CharField(label = "New Task")
    # you can add more fields like..
    # priority = forms.IntegerField(label = "Priority", min_value = 1, max_value=10 )

def index(request):
    if "tasks" not in request.session:
        request.session["tasks"]=[]

    return render(request, "tasks/index.html", {
        "tasks": request.session["tasks"]
    })

def add(request): 
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request, "tasks/add.html", {
        "form": form    #exhisting form
}) 

    return render(request, "tasks/add.html", {
        "form": NewTaskForm()
}) 