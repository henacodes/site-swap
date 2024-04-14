from django.shortcuts import render
from .models import Website
# Create your views here.




def site_list(request):

    sites = Website.objects.all()

    return render(request, "website/sites.html", { "sites":sites })