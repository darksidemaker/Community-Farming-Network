from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


def logout_view(request):
    logout(request)

@login_required
def home(request):
    return render(request,"home.html",{})

def authView(request):
    if request.method== "POST":
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
    else:
        form = UserCreationForm()   

    return render(request,"registration/signup.html",{"form":form})