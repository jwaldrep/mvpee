from django.conf.urls import include, url
from django.contrib import admin

from pottytimer import views


urlpatterns = [
    # Examples:
    # url(r'^$', 'pottytime.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.home_page, name='home'),
    # url(r'^admin/', include(admin.site.urls)),
]
