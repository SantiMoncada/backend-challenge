from rest_framework import serializers
from assistance.models import Assistance


class AssistanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assistance
        fields = ['id', 'email', 'topic', 'address']
