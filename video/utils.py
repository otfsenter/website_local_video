from . import models


def get_vides_list():
    video_list = models.VideosModel.objects.all().values()

    # [{'id': 1, 'name': 'xingjimihang', 'alias': '星际迷航：皮卡德.Star.Trek.Picard'}, {'id': 2, 'name': 'siwangbiji', 'alias': '死亡笔记'}]
    video_list = list(video_list)

    new_video_list = []
    for each_video_dict in video_list:
        alias = each_video_dict.get('alias', '')
        name = each_video_dict.get('name', '')
        new_video_list.append([alias, name])

    return new_video_list


def from_video_name_get_number(video_name):
    video_list = models.DetailModel.objects.all().values()

    # [{'id': 1, 'alias': '星际迷航：皮卡德.Star.Trek.Picard', 'name': 'xingjimihang', 'numbers': '1,2,3,4'}]
    video_list = list(video_list)
    print(video_list)

    for each_video_dict in video_list:
        print('video_name: ', video_name)
        name = each_video_dict.get('name', '')
        print('name: ', name)
        if name == video_name:
            numbers = each_video_dict.get('numbers', '')
            alias = each_video_dict.get('alias', '')
            number_list = str(numbers).split(',')
            return number_list, alias, name
