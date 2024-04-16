from django.shortcuts import render, redirect
from .models import Website
from .forms import WebsiteForm
from .models import Website
from django.core.exceptions import ObjectDoesNotExist






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
    


def site_details(request, site_id):
    try:
        site = Website.objects.get(id=site_id)
        return render(request, "website/site_details.html", { "site":site })
    except Website.DoesNotExist:
        return render(request, "website/404.html")
