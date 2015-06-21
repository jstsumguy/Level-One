from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = patterns('',

	url(r'^(?P<article_id>\d+)/$', 'articles.views.article'),
	url(r'^static/(?P<article_path>\w+)/$', 'articles.views.static_article'),
	
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
