from django.shortcuts import render, redirect
from .forms import CreateUserForm
# Create your views here.



def create_user_view(request):
    if (request.method == "POST"):
        form = CreateUserForm(request.POST)
        if (form.is_valid):
            form.save()
            redirect("user_login")
    else:
        form = CreateUserForm()
        return render(request, "user/create_user.html", { "form":form })
