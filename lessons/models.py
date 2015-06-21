from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Level(models.Model):
	level = models.IntegerField(default=0)
	xp =  models.IntegerField(default=0)

class Student(models.Model):
	allow_email = models.BooleanField(default=True)
	user = models.OneToOneField(User)
	level = models.OneToOneField(Level)

	def __unicode__(self):
		return self.user.username

class Course(models.Model):
	'''
		Course types:
		0 = default
		1 = programming
		2 = web dev
		3 = ui/ux design
		4 = beta
	'''
	name = models.CharField(max_length=200)
	description = models.TextField(default="")
	quick_description = models.CharField(max_length=400, default="")
	course_type = models.IntegerField(default=0)
	author = models.ForeignKey(Student, null=True)
	user = models.ManyToManyField(User, null=True, blank=True)

	def __unicode__(self):
		return self.name

class Movie(models.Model):
	title = models.CharField(max_length=100, default="")
	url = models.CharField(max_length=500)

class Lesson(models.Model):
	name = models.CharField(max_length=100, default='none')
	movie = models.ForeignKey(Movie, null=True)
	content = models.TextField(null=True, default="You haven't added any content yet")
	rating = models.IntegerField(default=1)
	description = models.TextField(default="")
	course = models.ForeignKey(Course)
	created = models.DateTimeField(null=True)
	complete = models.BooleanField(default=False)

	def __unicode__(self):
		return self.name

class Quiz(models.Model):
	name = models.CharField(max_length=200)
	due_date = models.DateTimeField(null=True)
	lesson = models.ForeignKey(Lesson)

	def __unicode__(self):
		return self.name

class Multiple_Choice_Question(models.Model):
	question = models.CharField(max_length=1000)
	quiz = models.ForeignKey(Quiz)

class True_False_Question(models.Model):
	question = models.CharField(max_length=1000)
	answer = models.BooleanField(default=False)
	quiz = models.ForeignKey(Quiz, null=True)

class Quiz_Question_Choice(models.Model):
	question_type = models.IntegerField(default=0)
	choice = models.CharField(max_length=800)
	mcq = models.ForeignKey(Multiple_Choice_Question, null=True)
	answer = models.BooleanField(default=False)

class Article(models.Model):
	'''
	 0 = static
	 1 = dynamic
	'''
	name = models.CharField(max_length=200)
	author = models.ForeignKey(Student, null=True)
	article_type = models.IntegerField(default=0)
	content = models.TextField(null=True, default="")
	updated = models.DateTimeField(auto_now=True)
	path = models.CharField(max_length=500, null=True)

	def __unicode__(self):
		return self.name

class Course_Time(models.Model):
	student = models.ForeignKey(Student)
	course = models.ForeignKey(Course)
	start_date = models.DateTimeField(null=True)
	end_date = models.DateTimeField(null=True)

class Quiz_Score(models.Model):
	quiz = models.ForeignKey(Quiz)
	student = models.ForeignKey(Student)
	updated = models.DateTimeField(auto_now=True, default=datetime.now())
	score = models.IntegerField(default=0)

class Event(models.Model):
	name = models.CharField(max_length=200)
	start_date = models.DateTimeField()
	end_date = models.DateTimeField()
	students = models.ManyToManyField(Student)

class Lesson_Question(models.Model):
	student = models.ForeignKey(Student)
	question = models.CharField(max_length=800)
	lesson = models.ForeignKey(Lesson)

	def __unicode__(self):
		return self.question

class Lesson_Question_Answer(models.Model):
	student = models.ForeignKey(Student)
	question = models.ForeignKey(Lesson_Question)
	answer = models.TextField()

class Lesson_Question_Like(models.Model):
	likes = models.IntegerField(default=0)
	student = models.ForeignKey(Student)
	question = models.ForeignKey(Lesson_Question, null=True)

class Lesson_Answer_Like(models.Model):
	likes = models.IntegerField(default=0)
	student = models.ForeignKey(Student)
	answer = models.ForeignKey(Lesson_Question_Answer, null=True)

class Lesson_Progress(models.Model):
	complete = models.BooleanField(default=False)
	lesson = models.ForeignKey(Lesson)
	student = models.ForeignKey(Student)

class Course_Lesson_Activity(models.Model):
	lesson = models.ForeignKey(Lesson)
	student = models.ForeignKey(Student, null=True)
	visited = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.lesson.name + '--' + str(self.visited)

class Post(models.Model):
	content = models.TextField()
	publish_date = models.DateTimeField(null=True, auto_now=True)
	likes = models.IntegerField(null=True, default=0)
	user = models.ForeignKey(User)

class Review(models.Model):
	rating = models.IntegerField()
	description = models.TextField()
	course = models.ForeignKey(Course)
	student = models.ForeignKey(Student)

	def __unicode__(self):
		return self.course.name

class Challenge(models.Model):
	'''
		0 = daily challenge
		1 = competitive challenge
	'''
	title = models.CharField(max_length=200)
	challenge_type = models.IntegerField(default=0)
	description = models.TextField()
	content = models.TextField()
	created = models.DateTimeField(null=True)

	def __unicode__(self):
		return self.title

class Challenge_Score(models.Model):
	student = models.ForeignKey(Student)
	score = models.IntegerField(null=True, default=0)
	challenge = models.ForeignKey(Challenge)
	comments = models.TextField(null=True)

	def __unicode__(self):
		return self.student.user.username + ' ' + self.challenge.title

class Student_Lesson_Project(models.Model):
	title = models.CharField(max_length=200)
	student = models.ForeignKey(Student)
	lesson = models.ForeignKey(Lesson)
	source = models.TextField()

class Lesson_Project(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField()
	lesson = models.ForeignKey(Lesson)

class Notification(models.Model):
	student = models.ForeignKey(Student)
	viewed = models.BooleanField(default=False)
	message = models.CharField(max_length=500)
	created = models.DateTimeField(null=True)






















