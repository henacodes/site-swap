from django.shortcuts import render, redirect
from .models import Website
from .forms import WebsiteForm

# Create your views here.




def site_list(request):

    sites = Website.objects.all()

    return render(request, "website/sites.html", { "sites":sites })



def create_site(request):
    
    if(request.method == "POST"):
        form = WebsiteForm(request.POST, request.FILES)
        if (form.is_valid()):
            form.save()
            newsite = form.save(commit=False)
            newsite.posted_by = request.user
            newsite.save()
        
            return redirect("site_list")
    else:
        form = WebsiteForm()
        return render(request, 'website/create_site.html', {'form': form})