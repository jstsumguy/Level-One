# Django modules
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, Http404
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Count
from django.db.models import Q
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from django.core.paginator import Paginator
from django.core.mail import EmailMessage
from collections import Counter
from lessons.models import *
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from elearn import settings
import sys
import re
import json
import cgi
import httplib
import urllib
import urllib2
import time
import datetime
import random
import json
import itertools
import heapq
import os

# Helper functions
def get_student_level(student):
	if type(student) != None:
		return student.level.level, student.level.xp
	return None

# end helper

@login_required
def article(request, article_id):
	u = User.objects.get(id=request.user.id)
	s = Student.objects.get(user=u)
	level, xp = get_student_level(s)
	article = Article.objects.get(id=article_id)
	return render(request, 'articles/article.html', {
													'student': s,
													'level': level,
													'xp': xp,
													'article': article
												})

@login_required
def static_article(request, article_path):
	print 'path', article_path
	return render(request, 'articles/%s.html' % article_path)
