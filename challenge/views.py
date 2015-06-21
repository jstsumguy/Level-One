# Django modules
from django.shortcuts import render, redirect
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
from collections import Counter
from lessons.models import *
from django.contrib.auth.models import User
from elearn import settings
# Standard modules
import sys
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

def increment(student, val):
	xp = student.level.xp 
	if (xp + val) >= 100:
		print 'next level'
		student.level.level += 1
		student.level.xp = 0
	else:
		student.level.xp += val
	student.level.save()
	student.save()
	return

@login_required
def daily_challenge(request):
	u = User.objects.get(id=request.user.id)
	s = Student.objects.get(user=u)
	rep = s.rep
	submited = False
	c = None

	if Challenge.objects.filter(challenge_type=0).exists():
		c = Challenge.objects.filter(challenge_type=0).latest('created')
		if Challenge_Score.objects.filter(student=s, challenge=c).exists():
			submited = True
	return render(request, 'challenge/daily_challenge.html', {
															'user': u,
															'rep': rep,
															'student': s,
															'challenge': c,
															'submitted': submited
														})

@login_required
@csrf_exempt
def upload_challenge_solution(request):
	if request.method == 'POST':
		challenge_id = request.POST.get('id', '')
		print challenge_id
		u = User.objects.get(id=request.user.id)
		s = Student.objects.get(user=u)
		c = Challenge.objects.get(id=challenge_id)
		stream = request.FILES['upload'].readlines()
		file_name = request.FILES['upload'].name

		if 'pdf' in request.FILES['upload'].name:
			score = Challenge_Score(student=s, score=0, challenge=c)
			score.save()
			with open(settings.SOLUTION + str(score.id) + '_' + request.FILES['upload'].name, 'wb+') as destination:
				for line in stream:
					destination.write(line)
			increment(s, 5)
			return redirect('/challenge/compete/')
		return HttpResponseBadRequest("must be pdf")

@login_required
def compete(request):
	u = User.objects.get(id=request.user.id)
	s = Student.objects.get(user=u)
	submited = False
	c = None

	if Challenge.objects.filter(challenge_type=1).exists():
		c = Challenge.objects.filter(challenge_type=1).latest('created')
		print c.title
		if Challenge_Score.objects.filter(student=s, challenge=c).exists():
			submited = True
	scores = [ score for score in Challenge_Score.objects.filter(student=s)]
	solutions = [ {'user': cs.student.user.username, 'score': cs.score, 'rank': cs.student.level.level } for cs in Challenge_Score.objects.filter(challenge=c)][:10]
	return render(request, 'challenge/compete.html', {
															'user': u,
															'student': s,
															'scores': scores,
															'challenge': c,
															'submitted': submited,
															'solutions': solutions
														})

@login_required
def score(request, challenge_id):
	if Challenge.objects.filter(id=challenge_id).exists():
		c = Challenge.objects.get(id=challenge_id)
		u = User.objects.get(id=request.user.id)
		s = Student.objects.get(user=u)
		if Challenge_Score.objects.filter(student=s, challenge=c).exists():
			score = Challenge_Score.objects.get(student=s, challenge=c)
			return render(request, 'challenge/score.html', {'score': score, 'challenge': c, 'rp': '../../..', 'user': u })
	return HttpResponseBadRequest("Does not exist")





