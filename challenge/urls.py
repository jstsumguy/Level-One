from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = patterns('',

	url(r'^$', 'challenge.views.daily_challenge'),
	url(r'^upload_challenge_solution/$', 'challenge.views.upload_challenge_solution'),
	url(r'^compete/$', 'challenge.views.compete'),
	url(r'^score/(?P<challenge_id>\d+)/$', 'challenge.views.score'),
	
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
