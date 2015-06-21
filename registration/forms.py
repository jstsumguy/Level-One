from django import forms

# Sign up form
class SignUpForm(forms.Form):
	username = forms.CharField(max_length=100)
	email = forms.CharField(max_length=200)
	password = forms.CharField(max_length=200)