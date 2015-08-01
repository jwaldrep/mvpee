from django.conf.urls import include, url
from django.contrib import admin

from pottytimer import views


urlpatterns = [
    # Examples:
    # url(r'^$', 'pottytime.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.home_page, name='home'),
    url(r'^charts/new$', views.new_chart, name='new_chart'),
    url(r'^charts/(\d+)/$', views.view_chart, name='view_chart'),
    url(r'^charts/(\d+)/add_sticker$', views.add_sticker, name='add_sticker')
    # url(r'^admin/', include(admin.site.urls)),
]
