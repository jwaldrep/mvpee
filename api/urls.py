from rest_framework import routers

from .views import StickerViewSet


router = routers.DefaultRouter()
router.register(r'stickers', StickerViewSet)
