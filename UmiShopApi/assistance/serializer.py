from rest_framework import serializers
from assistance.models import Assistance


class assistanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assistance
        fields = ['email', 'topic', 'address']
