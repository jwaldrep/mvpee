from django.conf.urls import url

from .views import new_chart, view_chart, add_sticker

urlpatterns = [
    url(r'^new$', new_chart, name='new_chart'),
    url(r'^(\d+)/$', view_chart, name='view_chart'),
    url(r'^(\d+)/add_sticker$', add_sticker, name='add_sticker'),
]
