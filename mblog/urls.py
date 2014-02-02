from django.contrib import admin
admin.autodiscover()

from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login

from mblog.views import current_time
from mblog.views import hours_ahead
from mblog.views import hello
from mblog.views import display_meta
from mblog.views import search_form
from mblog.views import search
from mblog.views import register
from mblog.views import main
from mblog.views import logout
from mblog.views import profile
from mblog.views import password

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', main),
    url(r'^register$', register),
    url(r'^login$', login, {'template_name': 'login.html'}),
    url(r'^logout$', logout),
    url(r'^profile$', profile),
    url(r'^password$', password),
    url(r'^time/plus/(\d{1,2})/$', hours_ahead),
    url(r'^hello/$', hello),
    url(r'^show/$', display_meta),
    url(r'^search-form/$', search_form),
    url(r'^search/$', search),
)
