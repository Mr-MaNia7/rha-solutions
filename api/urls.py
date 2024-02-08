from django.urls import path
from .views import api_main, api_update

urlpatterns = [

    path("", api_main.as_view()),
    path("<str:track_number>/", api_update.as_view())

]