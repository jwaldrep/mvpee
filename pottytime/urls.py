from django.conf.urls import include, url
from django.contrib import admin

from pottytimer import views as pt_views
from pottytimer import urls as pt_urls


urlpatterns = [
    # Examples:
    # url(r'^$', 'pottytime.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', pt_views.home_page, name='home'),
    url(r'^charts/', include(pt_urls)),
    # url(r'^admin/', include(admin.site.urls)),
]
