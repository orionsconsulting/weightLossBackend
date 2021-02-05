from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
from weightLoss.models import WeightTracker
from weightLoss.serializers import WeightTrackerSerializer


class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def weight_tracker_list(request, pk):
    if request.method == 'GET':
        weight_list = WeightTracker.objects.filter(user_id=pk)
        weight_list_serializer = WeightTrackerSerializer(weight_list, many=True)
        return JSONResponse(weight_list_serializer.data)
