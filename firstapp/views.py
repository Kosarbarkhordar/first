from re import template
from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from django.template import loader

def index (request):
    return  HttpResponse('man daram yad migiram:)')

days={
    'sunday':'rozhafte1',
    'mounday':'rozhafte2',
    'tersday':'rozhafte3',
    'friday':'rozhafte4',
}
def dynamic_day (request):
    day_data=days.get(day)
    return HttpResponse(day_data)