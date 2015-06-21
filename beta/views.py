from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, Http404, HttpResponseRedirect
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

def check_for_media(course_id, lesson_id, movie_title):
	media_root = os.getcwd() + '/media/'
	directory = None
	if os.path.exists(media_root + course_id):
		directory = media_root + course_id + '/'
		if os.path.exists(directory + lesson_id):
			if os.path.exists(directory + lesson_id + '/' + movie_title + '.mp4'):
				return True
			else:
				return False
		else:
			os.makedirs(directory + lesson_id)
			check_for_media(course_id, lesson_id, movie_title)
	else:
		os.makedirs(media_root + course_id)
		check_for_media(course_id, lesson_id, movie_title)

def get_course_students(course):
	try:
		return len(course.user.all())
	except Exception as ex:
		pass
	return 0

def get_student_level(student):
	if type(student) != None:
		return student.level.level, student.level.xp
	return None

def format_type(t):
	if t == 0:
		return 'Default'
	elif t == 1:
		return 'Programming'
	elif t == 2:
		return 'Web Development'
	elif t == 3:
		return 'UI Design'
	elif t == 4:
		return 'Beta'
	return

@login_required
def beta(request):
	courses = []
	u = User.objects.get(id=request.user.id)
	s = Student.objects.get(user=u)
	level, xp = get_student_level(s)
	notifications = [n for n in Notification.objects.filter(student=s, viewed=False).order_by('-created')[:5]]
	courses = []
	for c in Course.objects.filter(author=s):
		obj = {}
		obj['id'] = c.id
		obj['name'] = c.name
		obj['type'] = format_type(c.course_type)
		obj['lessons'] = 0
		if Lesson.objects.filter(course=c).exists():
			obj['lessons'] = len(Lesson.objects.filter(course=c))
		courses.append(obj)
	return render(request, 'beta/beta.html', {
												'user': u,
												'courses': courses,
												'level': level,
												'notifications': notifications,
												'xp': xp })

@login_required
@csrf_exempt
def new_beta_course(request):
	json_data = json.loads(request.body)
	title = json_data['title']
	description = json_data['description']
	u = User.objects.get(id=request.user.id)
	s = Student.objects.get(user=u)
	try:
		c = Course(name=title, quick_description=description, author=s, course_type=4)
		c.save()
		return HttpResponse("success")
	except Exception as ex:
		print str(ex)
	return HttpResponse("fail")

@login_required
def beta_course(request, course_id):
	u = User.objects.get(id=request.user.id)
	s = Student.objects.get(user=u)
	level, xp = get_student_level(s)
	notifications = [n for n in Notification.objects.filter(student=s, viewed=False).order_by('-created')[:5]]
	course = Course.objects.get(id=course_id)
	lessons = Lesson.objects.filter(course=course).order_by
	print lessons
	return render(request, 'beta/course.html', {
												'rp': '../../..',
												'course': course,
												'lessons': lessons,
												'level': level,
												'notifications': notifications,
												'xp': xp })

@login_required
def lesson(request, course_id, lesson_id):
	if request.method == 'GET':
		# Store most recent visited lesson
		u = User.objects.get(id=request.user.id)
		s = Student.objects.get(user=u)
		project = None
		quiz = None
		course = Course.objects.get(id=course_id)
		lesson = Lesson.objects.get(id=lesson_id)
		students = get_course_students(course)
		submitted = False

		# Log lesson activity
		if not (Course_Lesson_Activity.objects.filter(student=s, lesson=lesson).exists()):
			cla = Course_Lesson_Activity(student=s, lesson=lesson)
			cla.save()
		else:
			cla = Course_Lesson_Activity.objects.get(student=s, lesson=lesson)
			cla.save()

		questions = []
		for q in Lesson_Question.objects.filter(lesson=lesson):
			obj = {}
			obj['question'] = q.question
			obj['likes'] = 0
			obj['id'] = q.id
			if Lesson_Question_Like.objects.filter(question=q).exists():
				likes = [ like.likes for like in Lesson_Question_Like.objects.filter(question=q)]
				likes = len(likes)
				print likes
				obj['likes'] = likes
			questions.append(obj)

		movies = [{'title': m.title, 'url': m.url } for m in Movie.objects.filter(lesson=lesson)]
		if Lesson_Project.objects.filter(lesson=lesson).exists():
			project = Lesson_Project.objects.get(lesson=lesson)
		if Quiz.objects.filter(lesson=lesson).exists():
			quiz = Quiz.objects.get(lesson=lesson)
			if Quiz_Score.objects.filter(quiz=quiz, student=s).exists():
				submitted = True

		return render(request, 'beta/lesson.html', {
														'user': u,
														'student': s,
														'students': students,
														'course': course, 
														'lesson': lesson, 
														'movies': movies,
														'quiz': quiz,
														'submitted': submitted,
														'questions': questions,
														'project': project })
	elif request.method == 'POST':
		movie_title = request.POST.get('movie_title', '')
		lesson_id = request.POST.get('lesson_id', '')
		stream = request.FILES['file']
		course_id = None
		print movie_title
		print lesson_id

		if Lesson.objects.filter(id=lesson_id).exists():
			lesson = Lesson.objects.get(id=lesson_id)
			course_id = str(lesson.course.id)
			if not lesson.movie:
				m = Movie(title=movie_title, url="")
				m.save()
				if not check_for_media(str(course_id), str(lesson_id), str(m.id)):
					with open(os.getcwd() + '/media/' + str(course_id) + '/' + str(lesson_id) + '/' + str(m.id) + '.mp4', 'w') as f:
						for chunk in stream.chunks():
							f.write(chunk)
					m.url = str(course_id) + '/' + str(lesson_id) + '/' + str(m.id) + '.mp4'
				m.save()
				lesson.movie =  m
			lesson.save()
		return HttpResponseRedirect('/beta/lesson/'+course_id+'/'+lesson_id+'/')

@csrf_exempt
@login_required
def edit_project(request):
	json_data = json.loads(request.body)
	lesson_id = json_data['lesson_id']
	content = json_data['content']

	if json_data.has_key('project_id'):
		project_id = json_data['project_id']
		p = Lesson_Project.objects.get(id=project_id)
		p.description = content
		p.save()
	else:
		lesson = Lesson.objects.get(id=lesson_id)
		p = Lesson_Project(title="lesson project", description=content, lesson=lesson)
		p.save()
	return HttpResponse("success")

	





























































