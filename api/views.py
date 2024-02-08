from rest_framework import generics
from atcom_incident_bot.models import Incident
from .serializers import IncidentSerializer

# Create your views here.
class api_main(generics.ListCreateAPIView):
    queryset = Incident.objects.all()
    serializer_class = IncidentSerializer

class api_update(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = "track_number"
    lookup_url_kwarg = "track_number"
    queryset = Incident.objects.all()
    serializer_class = IncidentSerializer

    def perform_update(self, serializer):
        track_number = self.kwargs.get(self.lookup_url_kwarg)
        serializer.save(track_number = track_number)