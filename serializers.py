from rest_framework import serializers
from .models import Activate
class activateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Activate
        fields = '__all__'
