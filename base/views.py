from django.shortcuts import render
from . import models
# Create your views here.

def Home(request):
    header = list(models.Header.objects.all())[-1]
    services = models.Service.objects.all()
    projects = models.Project.objects.all()
    features = models.Feature.objects.all()
    context = {
        'services': services,
        'projects': projects,
        'features': features,
        'header': header
        }
    return render(request, "base/home.html", context=context)
