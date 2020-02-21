from django.db import models


# Create your models here.

class VideosModel(models.Model):
    name = models.CharField(max_length=5000)
    alias = models.CharField(max_length=5000)

    class Meta:
        verbose_name_plural = '影视列表'


class DetailModel(models.Model):
    alias = models.CharField(max_length=5000)
    name = models.CharField(max_length=5000)
    numbers = models.CharField(max_length=5000)

    class Meta:
        verbose_name_plural = '电视剧集数'