from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                       url(r"^login/$", 'django.contrib.auth.views.login'),
                       url(r"^logout/$", 'django.contrib.auth.views.logout'),
                       url(r"^admin/", include(admin.site.urls)),
)
