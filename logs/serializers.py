from rest_framework import serializers
from .models import logs

class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = logs
        fields = '__all__'


