from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = patterns('',

    url(r'^signup/$', 'registration.views.signup_form'),
    url(r'^signup_complete/$', 'registration.views.signup'),
    url(r'^logout/$', 'registration.views.logout_user'),

    
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
