from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = patterns('',
	url(r'^$', 'beta.views.beta'),
	url(r'new_beta_course/$', 'beta.views.new_beta_course'),
	url(r'course/(?P<course_id>\d+)/$', 'beta.views.beta_course'),
	url(r'lesson/(?P<course_id>\d+)/(?P<lesson_id>\d+)/$', 'beta.views.lesson'),
	url(r'edit_project/$', 'beta.views.edit_project'),
	
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
