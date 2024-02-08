"""atcom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from atcom_incident_bot import urls as atcom_incident_bot_urls
# from to_be_deleted_bot import urls as to_be_deleted_bot_urls

urlpatterns = [
    path('@atcom/', admin.site.urls),
    path('', include("base.urls")),
    # path('atcom_incident_bot/', include(atcom_incident_bot_urls)),
    # path('to_be_deleted_bot/', include(to_be_deleted_bot_urls)),
    # path('api/', include("api.urls")),
]

admin.site.site_header = "RHA Website Admin"
admin.site.site_title = "Site Administration"
admin.site.index_title = "Welcome to RHA"
