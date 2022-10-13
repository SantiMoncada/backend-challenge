from django.http import JsonResponse
from rest_framework.parsers import JSONParser

from rest_framework.decorators import api_view

from assistance.serializer import assistanceSerializer
from .taks import contact_product


@api_view(['POST'])
def assistance(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = assistanceSerializer(data=data)
        if (serializer.is_valid()):
            contact_product.apply_async(([data]))
            return JsonResponse({"Msg": "Notification sent"}, status=200)
        else:
            return JsonResponse(serializer.errors, status=400)

    return JsonResponse({'errorMsg': 'Bad request'}, status=400)
