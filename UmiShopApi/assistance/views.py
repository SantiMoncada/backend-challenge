from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from .taks import contact_product


@csrf_exempt
def assistance(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        # TODO check for fields
        contact_product.apply_async(([data]))
        return JsonResponse({"Msg": "Notification sent"}, status=200)

    return JsonResponse({'errorMsg': 'Bad request'}, status=400)
