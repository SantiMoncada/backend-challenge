from django.http import JsonResponse
from rest_framework.parsers import JSONParser

from rest_framework.decorators import api_view

from assistance.models import Assistance
from assistance.serializer import AssistanceSerializer
from .taks import contact_product


@api_view(['GET', 'POST'])
def assistance(request):

    if request.method == 'GET':
        assistances = Assistance.objects.all()
        serializer = AssistanceSerializer(assistances, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AssistanceSerializer(data=data)
        if (serializer.is_valid()):
            serializer.save()
            contact_product.apply_async(([serializer.data]))
            return JsonResponse({"Msg": "Notification sent", 'Data': serializer.data}, status=200)
        else:
            return JsonResponse(serializer.errors, status=400)

    return JsonResponse({'errorMsg': 'Bad request'}, status=400)


@api_view(['GET', 'DELETE'])
def assistance_details(request, pk):
    try:
        assistance = Assistance.objects.get(pk=pk)
    except Assistance.DoesNotExist:
        return JsonResponse(data={}, status=404)

    if (request.method == 'GET'):
        serializer = AssistanceSerializer(assistance)
        return JsonResponse(serializer.data)

    elif request.method == 'DELETE':
        assistance.delete()
        return JsonResponse(data={}, status=204)
