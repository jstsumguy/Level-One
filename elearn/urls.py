from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import *

urlpatterns = patterns('',
    # Main
    url(r'^$', 'django.contrib.auth.views.login', {'template_name': 'registration/login.html'}),
    url(r'^profile/$', 'lessons.views.profile'),
    url(r'^about/$', 'lessons.views.about'),

    # Courses
    url(r'^edit_course/$', 'lessons.views.edit_course'),
    url(r'^courses/$', 'lessons.views.courses'),
    url(r'^course/(?P<course_id>\d+)/$', 'lessons.views.course'),
    url(r'^enrolled/course/(?P<course_id>\d+)/$', 'lessons.views.enrolled_course'),

    # Lessons
    url(r'^lesson/(?P<course_id>\d+)/(?P<lesson_id>\d+)/$', 'lessons.views.lesson'),
    url(r'^edit_lesson/$', 'lessons.views.edit_lesson'),
    url(r'^new_lesson/$', 'lessons.views.new_lesson'),
    url(r'^delete_lesson/$', 'lessons.views.delete_lesson'),
    url(r'^add_lesson_content/$', 'lessons.views.add_lesson_content'),

    # Assessments
    url(r'^new_quiz/$', 'lessons.views.new_quiz'),
    url(r'^assessment/(?P<lesson_id>\d+)/(?P<quiz_id>\d+)/$', 'lessons.views.assessment'),
    url(r'^submit_assessment/(?P<quiz_id>\d+)/$', 'lessons.views.submit_assessment'),
    url(r'^assessment_result/(?P<lesson_id>\d+)/(?P<quiz_id>\d+)/$', 'lessons.views.assessment_result'),

    # Events
    url(r'^events/$', 'lessons.views.events'),
    url(r'^register_event/$', 'lessons.views.register_event'),

    # Questions
    url(r'^new_question/$', 'lessons.views.new_question'),
    url(r'^new_answer/$', 'lessons.views.new_answer'),
    url(r'^like_question/$', 'lessons.views.like_question'),
    url(r'^like_answer/$', 'lessons.views.like_answer'),
    url(r'^lesson_question/(?P<lesson_id>\d+)/(?P<question_id>\d+)/$', 'lessons.views.lesson_question'),
    url(r'^add_question/$', 'lessons.views.add_question'),
    url(r'^add_tf_question/$', 'lessons.views.add_tf_question'),

    # Progress 
    url(r'^get_course_progress/(?P<course_id>\d+)/$', 'lessons.views.get_course_progress'),
    url(r'^update_lesson_progress/(?P<lesson_id>\d+)/$', 'lessons.views.get_course_progress'),

    # Actions
    url(r'^enroll/(?P<course_id>\d+)/$', 'lessons.views.enroll'),
    url(r'^unenroll/$', 'lessons.views.remove_course'),
    url(r'^get_ratings/$', 'lessons.views.get_ratings'),
    url(r'^set_rating/$', 'lessons.views.set_rating'),

    # Notifications 
    url(r'^notification_close/(?P<notification_id>\d+)/$', 'lessons.views.notification_close'),

    # Settings
	url(r'^settings/$', 'lessons.views.settings'),
	url(r'^change_settings/$', 'lessons.views.change_settings'),
	url(r'^update_notifications/$', 'lessons.views.update_notifications'),
	url(r'^get_notifications/$', 'lessons.views.get_notifications'),

    # Challenges
    url(r'^challenge/', include('challenge.urls')),

    # Articles
    url(r'^article/', include('articles.urls')),

    # Beta
    url(r'^beta/', include('beta.urls')),

    # Admin/Registration
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'registration/login.html'}),
    url(r'^static/', include(admin.site.urls)),
    url(r'^registration/', include('registration.urls')),

# Password Reset URLs:
    url(r'^accounts/password_reset/$', 'django.contrib.auth.views.password_reset',
    {'template_name': 'registration/password_reset_form.html'}, name="password_reset"),
    url(r'^accounts/password_reset/done/$', 'django.contrib.auth.views.password_reset_done',
     {'template_name': 'registration/password_reset_done.html'}, name='password_reset_done'),
    url(r'^accounts/password_reset/(?P<uidb64>[0-9A-Za-z]{1,13})-(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        'django.contrib.auth.views.password_reset_confirm', 
        {'template_name': 'registration/password_reset_confirm.html'},
        name='password_reset_confirm'),
    url(r'^accounts/password_reset/complete/$', 
        'django.contrib.auth.views.password_reset_complete',
        {'template_name': 'registration/password_reset_complete.html'},
         name='password_reset_complete'),


) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))
