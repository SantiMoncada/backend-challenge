from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'phone']

    # id = serializers.IntegerField(read_only=True)
    # name = serializers.CharField(required=True, allow_blank=False, max_length=100)
    # email = serializers.CharField(required=True, allow_blank=False, max_length=100)
    # phone  = serializers.CharField(required=True, allow_blank=False, max_length=100)

    # def create(self, validated_data):
    #     return User.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name',instance.name)
    #     instance.email = validated_data.zget('email',instance.email)
    #     instance.phone = validated_data.get('phone',instance.phone)

    #     instance.save()
    #     return instance
