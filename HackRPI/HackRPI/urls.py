from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'HackRPI.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'ConnHackEd.views.index', name='index'),

    url(r'^admin/', include(admin.site.urls)),


)
