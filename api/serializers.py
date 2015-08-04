from pottytimer.models import Sticker, Chart
from rest_framework import serializers

class StickerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sticker
        fields = ('id', 'url', 'text') # TODO: Add chart
