from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register([
    Project, Service, Feature, Header, Sender,
])


