from django.shortcuts import render

from pottytimer.models import Sticker, Chart
from api.serializers import StickerSerializer
from rest_framework import viewsets


class StickerViewSet(viewsets.ModelViewSet):
    queryset = Sticker.objects.all()
    serializer_class =StickerSerializer
