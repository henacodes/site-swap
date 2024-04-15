from django.shortcuts import render, redirect
from .forms import CreateUserForm, UserAuthenticateForm
# Create your views here.



def create_user_view(request):
    if (request.method == "POST"):
        form = CreateUserForm(request.POST)
        if (form.is_valid):
            form.save()
            redirect("login_user")
    else:
        form = CreateUserForm()
        return render(request, "user/create_user.html", { "form":form })


def login_user_view(request):
    if (request.method == "POST"):
        form = UserAuthenticateForm(request.POST)
    else:
        form = UserAuthenticateForm()
        return render(request, "user/login_user.html", {"form":form})