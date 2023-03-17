from django.shortcuts import render

# Create your views here.
tasks =["bar", "foo", "baz"]

def index(request):
    now = datetime.datetime.now()
    return render(request, "tasks/index.html",{
        "tasks": tasks,
    })