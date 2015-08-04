from rest_framework import routers

from .views import StickerViewSet, ChartViewSet


router = routers.DefaultRouter()
router.register(r'stickers', StickerViewSet)
router.register(r'charts', ChartViewSet)
