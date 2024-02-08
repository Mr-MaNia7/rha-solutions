from atcom_incident_bot.models import Incident, TelegramUser as User
from rest_framework import serializers

class TelegramUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['telegram_id', 'username', 'first_name']

class IncidentSerializer(serializers.ModelSerializer):
    assigned_to = TelegramUserSerializer(read_only=True)
    class Meta:
        model = Incident
        fields = [
                    'track_number',
                    'reporter',
                    'reason',
                    'error_type',
                    'desktop_id',
                    'desc',
                    'is_fixed',
                    'assigned_to'
                ]