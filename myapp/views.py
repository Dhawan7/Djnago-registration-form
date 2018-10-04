from django.shortcuts import render
from django.http import HttpResponse
from .forms import userForm

def index(request):
    form = userForm()
    if request.method == 'POST':
        form = userForm(data=request.POST)
        if form.is_valid():
            print("Validation Successfully")
            form.save()
            return HttpResponse("<h1 style='color:green'>Thanks For Registeration</h1>")
    return render(request,'index.html',{'uform':form})
