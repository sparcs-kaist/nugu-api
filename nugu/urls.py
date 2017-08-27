from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from apps.api import views

urlpatterns = [
    url(r'^public_users/$', views.user_public_list),
    url(r'^users/$', views.user_list),
    url(r'^users/(?P<pk>[A-Za-z0-9]+)$', views.user_detail),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', admin.site.urls)
]

urlpatterns = format_suffix_patterns(urlpatterns)