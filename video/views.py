from django.shortcuts import render
from . import models
from . import utils


# Create your views here.

def index(request):
    new_video_list = utils.get_vides_list()
    return render(request, 'index.html', context={'video_list': new_video_list})


def detail(request, video_name):
    number_list, alias, name = utils.from_video_name_get_number(video_name)
    return render(request, 'detail.html', context={
        'number_list': number_list,
        'alias': alias,
        'name': name
    })


def detail_num(request, video_name, num):
    number_list, alias, name = utils.from_video_name_get_number(video_name)
    return render(request, 'number.html', context={
        'number': num,
        'alias': alias,
        'name': name
    })
