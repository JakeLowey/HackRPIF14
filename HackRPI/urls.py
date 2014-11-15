from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',

    (r'^$', 'django.contrib.auth.views.login', {
        'template_name': 'index.html'
    }),

    url(r'^admin/', include(admin.site.urls)),
)
