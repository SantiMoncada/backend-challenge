from django.http import JsonResponse
from rest_framework.parsers import JSONParser

from rest_framework.decorators import api_view

from users.models import User
from users.serializers import User, UserSerializer

from .tasks import send_email


@api_view(['GET', 'POST'])
def user_list(request):
    if (request.method == 'GET'):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif (request.method == 'POST'):
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)

        if (serializer.is_valid()):
            send_email.apply_async([data], countdown=60)
            serializer.save()
            return JsonResponse(serializer.data, status=201)

        return JsonResponse(serializer.errors, status=400)


@api_view(['GET'])
def user_is_registered(request, email):
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        return JsonResponse(data={}, status=404)

    serializer = UserSerializer(user)
    return JsonResponse(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def user_details(request, pk):

    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return JsonResponse(data={}, status=404)

    if (request.method == 'GET'):
        serializer = UserSerializer(user)
        return JsonResponse(serializer.data)

    elif (request.method == 'PUT'):
        data = JSONParser().parse(request)
        serializer = UserSerializer(user, data=data)
        if (serializer.is_valid()):
            serializer.save()
            return JsonResponse(serializer.data)

        return JsonResponse(serializer.errors, status=404)

    elif request.method == 'DELETE':
        user.delete()
        return JsonResponse(data={}, status=204)
