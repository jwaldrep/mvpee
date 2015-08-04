from pottytimer.models import Sticker, Chart
from rest_framework import serializers

class StickerSerializer(serializers.HyperlinkedModelSerializer):
    chart_id = serializers.PrimaryKeyRelatedField(read_only=True) # Magic!

    class Meta:
        model = Sticker
        fields = ('id', 'url', 'text', 'chart', 'chart_id')

class ChartSerializer(serializers.HyperlinkedModelSerializer):
    sticker_set = StickerSerializer(many=True, read_only=True)

    class Meta:
        model = Chart
        fields = ('id', 'url', 'sticker_set')
