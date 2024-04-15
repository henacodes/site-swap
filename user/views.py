from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login

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



'''
def login_user_view(request):
    if (request.method == "POST"):
        form = AuthenticationForm(request.POST)
        if (form.is_valid()):
            print('successfully logged in ')

        else:
            print("formmmmmmmmmmmmmmm")
            print(request.POST)
            print("Get the fuck outa here ")
    else:
        form = AuthenticationForm()
        return render(request, "user/login_user.html", {"form":form})
    


'''


def login_user_view(request):
    if request.method == "POST":
        print('loggin in')
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')  # Assuming the email field is used as the username
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect("site_list")
            else:
                print('Invalid credentials')
                form.add_error(None, 'Invalid email or password')  # Add a custom non-field error
                # Re-render the login page with the form and errors
                return render(request, "user/login_user.html", {"form": form})
        else:
            print('Form validation error:', form.errors)
            form.add_error(None, 'Invalid email or password')  # Add a custom non-field error
            # Re-render the login page with the form and errors
            return render(request, "user/create_user.html", {"form": form})
            return redirect("create_user")
    else:
        form = AuthenticationForm()
    return render(request, "user/login_user.html", {"form": form})