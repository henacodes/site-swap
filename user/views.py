from django.shortcuts import render, redirect
from .forms import CreateUserForm, CustomAuthenticationForm, UserUpdateForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required




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
    if request.method == "POST":
        print('loggin in')
        form = CustomAuthenticationForm(request, data=request.POST)
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
        form = CustomAuthenticationForm()
    return render(request, "user/login_user.html", {"form": form})




@login_required
def update_user_view(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('site_list')  # Replace 'profile' with the URL name of the user profile view
    else:
        form = UserUpdateForm(instance=request.user)

    print(form)
    return render(request, 'user/edit_profile.html', {'form': form})

@login_required
def logout_user_view(request):
    if (request.method == "POST"):
        logout(request)
        redirect("user_login")