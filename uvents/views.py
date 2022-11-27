import json

from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse
from .models import *
from django.core.serializers import serialize
from django.views.decorators.csrf import csrf_exempt

import logging


def index(request):

    all_fans  = Fan.objects.all()
    types = Type.objects.all()

    fans =  serialize('json',all_fans)
    fans = json.loads(fans)


    for fan in fans:
        fan_options = FanOption.objects.filter(fan_id = fan['pk']).all()
        fan_options_serialize = json.loads(serialize('json', fan_options))




        fan['fan_options'] = fan_options_serialize
        fan['fan_type'] = [ fan_type.type_name for fan_type in types if fan_type.pk == fan['fields']['fan_type']]


    # fans = serialize('json', all_fans)
    return JsonResponse(fans, safe=False)

@csrf_exempt
def get_fans(request):


    dict = json.loads(request.body.decode('utf-8'))


    types = Type.objects.filter(type_name__in = (dict['keys'])).all()


    fans_query = Fan.objects.filter( fan_type__in = (t.id for t in types),

                                    fan_options__air_flow__lte = ( int(dict['air_flow']) + (
                                                    ( int(dict['air_flow']) * int(dict['air_flow_tolerance_above'] )) / 100  )) ,
                                    fan_options__air_flow__gte = ( int(dict['air_flow']) - (
                                                    ( int(dict['air_flow']) * int(dict['air_flow_tolerance_below'] )) / 100  )),


                                    fan_options__pressure__lte = ( int(dict['pressure']) + (
                                                    ( int(dict['pressure']) * int(dict['pressure_tolerance_above'] )) / 100  )),

                                    fan_options__pressure__gte = ( int(dict['pressure']) - (
                                                    ( int(dict['pressure']) * int(dict['pressure_tolerance_below'] )) / 100  ))



                                    )

    fans =  serialize('json',fans_query)
    fans = json.loads(fans)

    for i in fans:

        query_fan_options = FanOption.objects.filter(fan_id = i['pk']).all()
        query_fan_options_serialize =   serialize('json', query_fan_options)
        query_fan_options_serialize = json.loads(query_fan_options_serialize)

        i['fan_options'] = query_fan_options_serialize
        i['fan_type'] = [ fan_type.type_name for fan_type in types if fan_type.pk == i['fields']['fan_type']]

    return JsonResponse(fans, safe=False)