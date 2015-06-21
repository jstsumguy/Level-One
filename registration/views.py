from django.http import HttpResponse, HttpResponseBadRequest, Http404
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from collections import Counter
from lessons.models import *
from django.shortcuts import render, redirect
from django.contrib.auth.views import login, logout
from django.contrib.auth.models import User
from django.db.models import Q
import sys
import json
import time
import datetime

@csrf_exempt
def signup(request):
	json_data = json.loads(request.body)
	username = json_data['username']
	email = json_data['email']
	password = json_data['password']
	status = None

	if User.objects.filter(Q(username=username) | Q(email=email)).exists():
		status = "exists"
	else:
		u = User.objects.create_user(username, email, password)
		u.save()
		level = Level(level=0, xp=0)
		level.save()
		student = Student.objects.create(allow_email=True, user=u, level=level)
		student.save()
		status = "success"
	return HttpResponse(json.dumps(status))

@csrf_exempt
def signup_form(request):
	return render(request, 'registration/signup.html')

@login_required
@csrf_exempt
def logout_user(request):
	logout(request)
	return redirect('../../')
