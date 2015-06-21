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
def send_notification(student, message):
	try:
		n = Notification(student=student, message=message, viewed=False, created=datetime.datetime.now())
		n.save()
	except Exception as ex:
		print str(ex)
	return 

def get_course_students(course):
	try:
		return len(course.user.all())
	except Exception as ex:
		pass
	return 0

def increment(student, val):
	xp = student.level.xp 
	if (xp + val) >= 100:
		print 'next level'
		student.level.level += 1
		student.level.xp = 0
		formatted_msg = 'Level ' + str(student.level.level) + ' reached!'
		n = Notification(student=student, message=formatted_msg, viewed=False, created=datetime.datetime.now())
		n.save()
	else:
		student.level.xp += val
	student.level.save()
	student.save()
	return

def get_lesson_progress(course, student):
	progress = total = 0
	for lesson in Lesson.objects.filter(course=course):
		if Lesson_Progress.objects.filter(lesson=lesson, student=student, complete=True).exists():
			progress += 1
		total += 1
	if progress != 0:
		progress = (float(progress)/(total)) * 100
	return progress



def get_student_level(student):
	if type(student) != None:
		return student.level.level, student.level.xp
	return None

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

def get_reviews(c):
	reviews = [ {'user': review.student.user.username, 'rating': review.rating, 'description': review.description} for review in Review.objects.filter(course=c)[:3]]
	return reviews

# end helper

@login_required
def about(request):
	u = User.objects.get(id=request.user.id)
	s = Student.objects.get(user=u)
	rp = '..'
	return render(request, 'lessons/about.html', {'user': u, 'rp': rp})

@login_required
def profile(request):
	courses = []
	u = User.objects.get(id=request.user.id)
	s = Student.objects.get(user=u)
	level, xp = get_student_level(s)
	articles = [ a for a in Article.objects.all().order_by('-updated')[:5]]
	notifications = [n for n in Notification.objects.filter(student=s, viewed=False).order_by('-created')[:5]]
	scores = [ score for score in Quiz_Score.objects.filter(student=s).order_by('-updated')[:50]]
	beta = Course.objects.filter(author=s, course_type=4)

	if Course.objects.filter(user=u).exists():
		for c in Course.objects.filter(user=u):
			obj = {}
			obj['name'] = c.name
			obj['id'] = c.id
			obj['description'] = c.quick_description
			obj['course_type'] = c.course_type
			obj['progress'] = get_lesson_progress(c, s)
			courses.append(obj)

	return render(request, 'lessons/profile.html', {
													'user': u,
													'courses': courses,
													'level': level,
													'scores': scores,
													'articles': articles,
													'notifications': notifications,
													'beta': beta,
													'xp': xp })

@csrf_exempt
@login_required
def add_lesson_content(request):
	movie_title = request.POST.get('movie_title', '')
	lesson_id = request.POST.get('lesson_id', '')
	stream = request.FILES['file']
	course_id = None

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
		return redirect('../enrolled/course/' + course_id + '/')
	return HttpResponse("fail")


@csrf_exempt
@login_required
def edit_lesson(request):
	if request.method == 'POST':
		json_data = json.loads(request.body)
		content = json_data['content']
		lesson_id = json_data['lesson_id']

		if Lesson.objects.filter(id=lesson_id).exists():
			lesson = Lesson.objects.get(id=lesson_id)
			lesson.content = content
			lesson.save()
			return HttpResponse("success")
	return HttpResponseBadRequest()

@login_required
@csrf_exempt
def new_lesson(request):
	json_data = json.loads(request.body)
	course_id = json_data['course_id']
	title = json_data['title']
	description = json_data['description']
	u = User.objects.get(id=request.user.id)
	s = Student.objects.get(user=u)

	if Course.objects.filter(id=course_id).exists():
		c = Course.objects.get(id=course_id)
		lesson = Lesson(name=title, description=description, course=c, rating=1, created=datetime.datetime.now())
		lesson.save()
		try:
			n = Notification(student=s, viewed=False, message="You created a new lesson!", created=datetime.datetime.now())
			n.save()
		except Exception as ex:
			print str(ex)
		return HttpResponse("success")
	return HttpResponseBadRequest("does not exists")

@csrf_exempt
def delete_lesson(request):
	json_data = json.loads(request.body)
	lesson_id = json_data['lesson_id']
	if Lesson.objects.filter(id=lesson_id).exists():
		lesson = Lesson.objects.get(id=lesson_id)
		lesson.delete()
		return HttpResponse("success")
	return HttpResponseBadRequest("does not exists")

@login_required
def lesson(request, course_id, lesson_id):
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

	return render(request, 'lessons/lesson.html', {
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


@login_required
@csrf_exempt
def get_course_progress(request, course_id):
	u = User.objects.get(id=request.user.id)
	s = Student.objects.get(user=u)
	obj = lesson_obj = {}
	top_students = []
	most_recent = progress = None
	try:
		if Course.objects.filter(id=course_id).exists():
			c = Course.objects.get(id=course_id)
			progress = get_lesson_progress(c, s)	
			users = c.user.all()
			for i in users:
				if Student.objects.filter(user=i).exists():
					st = Student.objects.get(user=i)
					top_students.append({'username': i.username})
			for lesson in Lesson.objects.filter(course=c):
				if Course_Lesson_Activity.objects.filter(student=s, lesson=lesson).exists():
					cla = Course_Lesson_Activity.objects.get(student=s, lesson=lesson)
					if most_recent == None:
						most_recent = cla
					elif cla.visited > most_recent.visited:
						most_recent = cla
			if most_recent != None:
				lesson_obj['name'] = most_recent.lesson.name
				lesson_obj['description'] = most_recent.lesson.description
	except Exception as ex:
		print str(ex)
	return HttpResponse(json.dumps({'students': top_students, 'lesson': lesson_obj, 'progress': progress}))

@login_required
@csrf_exempt
def update_lesson_progress(request, lesson_id):
	u = User.objects.get(id=request.user.id)
	s = Student.objects.get(user=u)
	if Lesson.objects.filter(id=lesson_id).exists():
		l = Lesson.objects.get(id=lesson_id)
		try:
			progress = Lesson_Progress(complete=True, student_id=s, lesson=l)
			progress.save()
			return HttpResponse("success")
		except Exception as ex:
			print 'Progress exception ' + str(ex)
			return HttpResponse("fail")



@login_required
def lesson_question(request, lesson_id, question_id):
	rp = "../../.."
	answers = []
	u = User.objects.get(id=request.user.id)
	s = Student.objects.get(user=u)
	level = get_student_level(s)
	lesson = Lesson.objects.get(id=lesson_id)
	question = Lesson_Question.objects.get(id=question_id)

	if Lesson_Question_Answer.objects.filter(question=question).exists():
		for a in Lesson_Question_Answer.objects.filter(question=question):
			obj = {}
			obj['answer'] = a.answer
			obj['id'] = a.id
			obj['student'] = a.student.user.username
			obj['likes'] = 0
			if Lesson_Answer_Like.objects.filter(answer=a).exists():
				likes = len([like.likes for like in Lesson_Answer_Like.objects.filter(answer=a)])
				obj['likes'] = likes
			answers.append(obj)
	print 'answers', answers
	return render(request, 'lessons/lesson_question.html', {
													'student': s,
													'lesson': lesson, 
													'question': question,
													'level': level,
													'answers': answers,
													'rp': rp })

@csrf_exempt
@login_required
def add_question(request):
	json_data = json.loads(request.body)
	questions = json_data['questions']
	quiz_id = json_data['quiz']

	if Quiz.objects.filter(id=quiz_id).exists():
		q = Quiz.objects.get(id=quiz_id)
		for question in questions:
			mcq = Multiple_Choice_Question(question=question['content'], quiz=q)
			mcq.save()
			for choice in question['choices']:
				if choice != question['answer']:
					qc = Quiz_Question_Choice(question_type=1, choice=choice, mcq=mcq, answer=False)
					qc.save()
				else:
					qc = Quiz_Question_Choice(question_type=1, choice=choice, mcq=mcq, answer=True)
					qc.save()
	return HttpResponse("success")

@csrf_exempt
@login_required
def add_tf_question(request):
	json_data = json.loads(request.body)
	question = json_data['question']
	quiz_id = json_data['quiz']
	answer = json_data['answer']

	if Quiz.objects.filter(id=quiz_id).exists():
		q = Quiz.objects.get(id=quiz_id)
		try:
			if answer == 'true':
				answer = True
			else:
				answer = False
			tfq = True_False_Question(question=question, quiz=q, answer=answer)
			tfq.save()
			return HttpResponse("success")
		except Exception as ex:
			print str(ex)
	return HttpResponse("fail")

@csrf_exempt
def new_question(request):
	json_data = json.loads(request.body)
	content = json_data['question']
	student_id = json_data['student_id']
	lesson_id = json_data['lesson_id']

	if Student.objects.filter(id=student_id).exists():
		student = Student.objects.get(id=student_id)
		lesson = Lesson.objects.get(id=lesson_id)
		q = Lesson_Question(student=student, question=content, lesson=lesson)
		q.save()
		return HttpResponse("success")
	return HttpResponse("fail")

@csrf_exempt
def new_answer(request):
	json_data = json.loads(request.body)
	question_id = json_data['question']
	answer = json_data['answer']
	u = User.objects.get(id=request.user.id)
	s = Student.objects.get(user=u)

	if Lesson_Question.objects.filter(id=question_id).exists():
		q = Lesson_Question.objects.get(id=question_id)
		a = Lesson_Question_Answer(answer=answer, question=q, student=s)
		a.save()
		return HttpResponse("success")
	return HttpResponse("fail")

@login_required
@csrf_exempt
def like_question(request):
	json_data = json.loads(request.body)
	question_id = json_data['question_id']
	u = User.objects.get(id=request.user.id)
	s = Student.objects.get(user=u)

	if Lesson_Question.objects.filter(id=question_id).exists():
		q = Lesson_Question.objects.get(id=question_id)
		if not Lesson_Question_Like.objects.filter(question=q, student=s).exists():
			like = Lesson_Question_Like(question=q, student=s, likes=1)
			like.save()
			print 'updated'
			return HttpResponse("success")
		return HttpResponse("exists")
	return HttpResponse("fail")

@login_required
@csrf_exempt
def like_answer(request):
	json_data = json.loads(request.body)
	answer_id = json_data['answer_id']
	u = User.objects.get(id=request.user.id)
	s = Student.objects.get(user=u)

	if Lesson_Question_Answer.objects.filter(id=answer_id).exists():
		q = Lesson_Question_Answer.objects.get(id=answer_id)
		if not Lesson_Answer_Like.objects.filter(answer=q, student=s).exists():
			like = Lesson_Answer_Like(answer=q, student=s, likes=1)
			like.save()
			print 'updated'
			return HttpResponse("success")
		return HttpResponse("exists")
	return HttpResponse("fail")

@login_required
def assessment_result(request, lesson_id, quiz_id):
	u = User.objects.get(id=request.user.id)
	s = Student.objects.get(user=u)
	q = None
	rp = '../../..'
	i = 1
	mc_questions = []

	if Quiz.objects.filter(id=quiz_id).exists():
		q = Quiz.objects.get(id=quiz_id)
		qs = Quiz_Score.objects.filter(student=s, quiz=q)[0]
		lesson = Lesson.objects.get(id=lesson_id)
		
		if Multiple_Choice_Question.objects.filter(quiz=q).exists():
			for question in Multiple_Choice_Question.objects.filter(quiz=q):
				obj = {}
				obj['choices'] = []
				obj['question'] = question.question
				obj['answer'] = None
				if Quiz_Question_Choice.objects.filter(mcq=question):
					for choice in Quiz_Question_Choice.objects.filter(mcq=question):
						choice_obj = {}
						choice_obj['id'] = choice.id
						choice_obj['choice'] = choice.choice
						choice_obj['mcq'] = i
						if choice.answer:
							choice_obj['answer'] = True
							obj['answer'] = choice.choice
						obj['choices'].append(choice_obj)
				mc_questions.append(obj)
				i = i + 1
	return render(request, 'lessons/assessment_result.html', {
														'rp': rp, 
														'lesson': lesson,
														'quiz': q, 
														'student': s, 
														'mc_questions': mc_questions,
														'score': qs})
		

@login_required
def assessment(request, lesson_id, quiz_id):
	u = User.objects.get(id=request.user.id)
	s = Student.objects.get(user=u)
	q = None
	assessment = False
	score = None
	lesson = None
	q = None
	mc_questions = None
	rp = '../../..'
	i = 1
	mc_questions = []

	if Quiz.objects.filter(id=quiz_id).exists():
		q = Quiz.objects.get(id=quiz_id)
		lesson = Lesson.objects.get(id=lesson_id)
		tfq = True_False_Question.objects.filter(quiz=q)
		if Multiple_Choice_Question.objects.filter(quiz=q).exists():
			for question in Multiple_Choice_Question.objects.filter(quiz=q):
				obj = {}
				obj['choices'] = []
				obj['question'] = question.question
				obj['answer'] = None
				if Quiz_Question_Choice.objects.filter(mcq=question):
					for choice in Quiz_Question_Choice.objects.filter(mcq=question):
						choice_obj = {}
						choice_obj['id'] = choice.id
						choice_obj['choice'] = choice.choice
						choice_obj['mcq'] = i
						if choice.answer:
							obj['answer'] = choice.choice
						obj['choices'].append(choice_obj)
				mc_questions.append(obj)
				i = i + 1
		if Quiz_Score.objects.filter(quiz=q, student=s).exists():
			score = Quiz_Score.objects.get(quiz=q, student=s)
		return render(request, 'lessons/assessment.html', {
															'rp': rp, 
															'score': score,
															'lesson': lesson,
															'quiz': q, 
															'student': s, 
															'mc_questions': mc_questions,
															'tfq': tfq,
															'assessment': assessment})

@csrf_exempt
@login_required
def new_quiz(request):
	json_data = json.loads(request.body)
	name = json_data['name']
	lesson_id = json_data['lesson']
	date = json_data['date']
	success = False
	try:
		date = datetime.datetime.strptime(date, '%m/%d/%Y')
		lesson = Lesson.objects.get(id=lesson_id)
		q = Quiz(name=name, lesson=lesson, due_date=date)
		q.save()
		success = True
	except Exception as ex:
		print str(ex)
	return HttpResponse(success)

@csrf_exempt
@login_required
def submit_assessment(request, quiz_id):
	json_data = json.loads(request.body)
	answers = json_data['answers']
	tf_answers = json_data['tf_answers']
	u = User.objects.get(id=request.user.id)
	s = Student.objects.get(user=u)
	q = Quiz.objects.get(id=quiz_id)
	total = correct = 0
	# Multiple choice
	for answer in answers:
		if Quiz_Question_Choice.objects.get(id=answer):
			choice = Quiz_Question_Choice.objects.get(id=answer)
			if choice.answer:
				correct += 1
	# True/false
	for a in tf_answers:
		if True_False_Question.objects.get(id=a['id']):
			tfq = True_False_Question.objects.get(id=a['id'])
			if a['answer'] == str(tfq.answer):
				correct += 1

	total = (float(correct)/(len(answers) + len(tf_answers))) * 100
	score = Quiz_Score(quiz=q, student=s, score=int(total))
	score.save()
	if score >= 90:
		increment(s, 5)
	try:
		progress = Lesson_Progress(lesson=q.lesson, student=s, complete=True)
		progress.save()
	except Exception as ex:
		print str(ex)
	return HttpResponse("success")

@csrf_exempt
@login_required
def edit_course(request):
	json_data = json.loads(request.body)
	course_id = json_data['course_id']
	content = json_data['content']

	if Course.objects.filter(id=course_id).exists():
		course = Course.objects.get(id=course_id)
		course.description = content
		course.save()
		return HttpResponse("success")
	return HttpResponse("fail")


@login_required
def course(request, course_id):
	if Course.objects.filter(id=course_id).exists():
		enrolled = False
		u = User.objects.get(id=request.user.id)
		s = Student.objects.get(user=u)
		course = Course.objects.get(id=course_id)
		students = get_course_students(course)
		if Course.objects.filter(id=course_id, user=u).exists():
			enrolled = True
		reviews = get_reviews(course)
		print 'reviews', reviews
		print 'enrolled', enrolled
		notifications = [n for n in Notification.objects.filter(student=s, viewed=False).order_by('-created')[:5]]
		return render(request, 'lessons/course.html', {
														'user': u,
														'course': course,
														'rp': '../..',
														'enrolled': enrolled,
														'students': students,
														'notifications': notifications,
														'reviews': reviews
														})
	return HttpResponseBadRequest()

@login_required
def enrolled_course(request, course_id):
	rp = '../../..'
	u = User.objects.get(id=request.user.id)
	s = Student.objects.get(user=u)
	c = Course.objects.get(id=course_id)
	students = get_course_students(c)
	falsy = 0
	lessons = []
	for lesson in Lesson.objects.filter(course=c):
		obj = {}
		obj['id'] = lesson.id
		obj['name'] = lesson.name
		obj['description'] = lesson.description
		obj['complete'] = False
		if Lesson_Progress.objects.filter(lesson=lesson, student=s, complete=True).exists():
			obj['complete'] = True
		if obj['complete'] == False:
			falsy += 1
		if falsy == 2:
			break
		lessons.append(obj)
	return render(request, 'lessons/enrolled_course.html', {
															'course': c,
															'lessons': reversed(lessons),
															'students': students,
															'rp': rp })

@login_required
def courses(request):
	u = User.objects.get(id=request.user.id)
	rp = "../.."
	courses = Course.objects.all()
	return render(request, 'lessons/courses.html', {'user': u, 'courses': courses, 'rp': rp})

@login_required
@csrf_exempt
def enroll(request, course_id):
	u = User.objects.get(id=request.user.id)
	s = Student.objects.get(user=u)
	if Course.objects.filter(id=course_id).exists():
		c = Course.objects.get(id=course_id)
		c.user.add(u)
		c.save()

		# Send notification 
		send_notification(s, str(c.name) + ' added!')
		return HttpResponse("success")
	else:
		return HttpResponse("fail")

@login_required
@csrf_exempt
def remove_course(request):
	json_data = json.loads(request.body)
	course_id = json_data['course']
	u = User.objects.get(id=request.user.id)
	s = Student.objects.get(user=u)
	if Course.objects.filter(id=course_id).exists():
		c = Course.objects.get(id=course_id)
		c.user.remove(u)
		c.save()
		return HttpResponse("success")
	return HttpResponse("fail")

@csrf_exempt
def get_ratings(request):
	json_data = json.loads(request.body)
	lessons = json_data['lessons']
	ratings = []
	for item in lessons:
		lesson = Lesson.objects.get(id=item)
		obj = {'id': lesson.id, 'rating': lesson.rating}
		ratings.append(obj)
	return HttpResponse(json.dumps(ratings))

@csrf_exempt
def set_rating(request):
	json_data = json.loads(request.body)
	lesson_id = json_data['lesson_id']
	value = json_data['value']
	if Lesson.objects.filter(id=lesson_id).exists():
		lesson = Lesson.objects.get(id=lesson_id)
		lesson.rating = value
		lesson.save()
		return HttpResponse("success")
	return HttpResponseBadRequest()


@csrf_exempt
@login_required
def change_settings(request):
	json_data = json.loads(request.body)
	first_name = json_data['firstname']
	last_name = json_data['lastname']
	email = json_data['email']

	if User.objects.filter(id=request.user.id).exists():
		u = User.objects.get(id=request.user.id)
		u.first_name = first_name
		u.last_name = last_name
		u.email = email
		u.save()
		return HttpResponse("success")
	return HttpResponseBadRequest()

@login_required
def settings(request):
	u = None
	if User.objects.filter(id=request.user.id).exists():
		u = User.objects.get(id=request.user.id)
	return render(request, 'lessons/settings.html', {'user': u, 'rp': '..' })

@login_required
@csrf_exempt
def update_notifications(request):
	json_data = json.loads(request.body)
	state = json_data['state']
	u = User.objects.get(id=request.user.id)
	if u.student:
		if state:
			u.student.allow_email = True
		else:
			u.student.allow_email = False
		u.student.save()
	return HttpResponse("success")

@login_required
@csrf_exempt
def get_notifications(request):
	u = User.objects.get(id=request.user.id)
	if u.student.allow_email:
		return HttpResponse(True)
	return HttpResponse(False)

@login_required
def progress(request):
	u = User.objects.get(id=request.user.id)
	s = Student.objects.get(user=u)
	rp = '..'
	return render(request, 'lessons/progress.html', {'user': u, 'student': s, 'rp': rp})

@login_required
@csrf_exempt
def events(request):
	u = User.objects.get(id=request.user.id)
	s = Student.objects.get(user=u)
	e = Event.objects.all()[0]
	rp = '..'
	reg = False
	if s in e.students.all():
		reg = True
	return render(request, 'lessons/events.html', {'event': e, 'user': u, 'student': s, 'rp': rp, 'registered': reg})

@csrf_exempt
@login_required
def register_event(request):
	json_data = json.loads(request.body)
	event_id = json_data['id']

	u = User.objects.get(id=request.user.id)
	s = Student.objects.get(user=u)

	if Event.objects.filter(id=event_id).exists():
		event = Event.objects.get(id=event_id)
		if not s in event.students.all():
			event.students.add(s)
		event.save()

		mail('Please follow this link to complete registration:  https://docs.google.com/forms/d/1R6-0clFVYdHeOHCm2bbYQnVTP3CP7TfKYDoKARbqoi0/viewform?usp=send_form', 'event', u.email)
		return HttpResponse("success")
	return HttpResponse("fail")

@csrf_exempt
@login_required
def notification_close(request, notification_id):
	if Notification.objects.filter(id=notification_id).exists():
		n = Notification.objects.get(id=notification_id)
		n.viewed = True
		n.save()
		return HttpResponse("success")
	return HttpResponse("fail")

def mail(message, subject, recipient_address):
	email = EmailMessage(subject, message, to=[recipient_address])
	email.send()






