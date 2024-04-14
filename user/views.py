from django.shortcuts import render
from .forms import CreateUserForm
# Create your views here.



def create_user_view(request):
    if (request.method == "POST"):
        form = CreateUserForm(request.POST)
        print("foorm is populated")
    else:
        form = CreateUserForm()
        return render(request, "user/create_user.html", { "form":form })
