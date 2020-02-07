from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import json
import math as m
from django.http import JsonResponse
# Create your views here.


def circle_distance(lati_1, lati_2, long_1, long_2):
    lati_1 = m.radians(lati_1)
    lati_2 = m.radians(lati_2)
    long_1 = m.radians(long_1)
    long_2 = m.radians(long_2)
    d_long = long_2 - long_1
    x = (m.sin(lati_1)*m.sin(lati_2))+(m.cos(lati_1)*m.cos(lati_2)*m.cos(d_long))
    distance = m.acos(x) * 6371
    return distance
'''
@api_view(['POST'])
def CustomersAround(request):
    try:
        file = request.data['file']
        Office_lati = float(request.data['latitude'])
        Office_long = float(request.data['longitude'])
        customers_list = file.read().decode('utf8').replace("'", '"')
        customers_list = '['+customers_list.replace('\n', ',')+']'
        c_around = []
        for i in json.loads(customers_list):
            C_lati = float(i['latitude'])
            C_long = float(i['longitude'])
            distance = circle_distance(Office_lati, C_lati, Office_long, C_long)
            if distance <=100:
                customer = {'user_id':i['user_id'], 'name':i['name']}
                c_around.append(customer)

        for i in range(len(c_around)-1):
            for j in range(len(c_around)-i-1):
                if c_around[j]['user_id'] > c_around[j+1]['user_id']:
                    c_around[j], c_around[j+1] = c_around[j+1], c_around[j]

    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'POST':
        return JsonResponse({'data':c_around})
'''

@api_view(['POST'])
def CustomersAround(request):
    try:
        file = request.data['file']
        Office_lati = float(request.data['latitude'])
        Office_long = float(request.data['longitude'])
        customers_list = file.read().decode('utf8').replace("'", '"')
        list = customers_list.split('\n')
        c_around = []
        for i in list:
            customer = json.loads(i)
            C_lati = float(customer['latitude'])
            C_long = float(customer['longitude'])
            distance = circle_distance(Office_lati, C_lati, Office_long, C_long)
            if distance <=100:
                x = {'user_id':customer['user_id'], 'name':customer['name']}
                c_around.append(x)

        for i in range(len(c_around)-1):
            for j in range(len(c_around)-i-1):
                if c_around[j]['user_id'] > c_around[j+1]['user_id']:
                    c_around[j], c_around[j+1] = c_around[j+1], c_around[j]
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'POST':
        return JsonResponse({'data':c_around})
