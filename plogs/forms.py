from django import forms
from django.contrib.auth.models import User 

class RegisterForm(forms.Form):
	username  = forms.CharField(widget=forms.TextInput(
					attrs={"class":"form-control"
					,"placeholder":"Username"}))
	email     = forms.EmailField(widget=forms.TextInput(
						attrs={"class":"form-control"
						,"placeholder":"Email"}))
	password  = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"
						,"placeholder":"password"}))
	password2 = forms.CharField(label='confirm password',
		              widget=forms.PasswordInput(attrs={"class":"form-control"
						,"placeholder":"confirm password"}))

	def clean_username(self):
		username= self.cleaned_data.get('username')
		qs = User.objects.filter(username=username)
		if qs.exists():
			raise forms.ValidationError('user name is taken')
		return username
	def clean_email(self):
		email= self.cleaned_data.get('email')
		qs = User.objects.filter(email=email)
		if qs.exists():
			raise forms.ValidationError('email name is taken')
		return email
	def clean(self):
		data      = self.cleaned_data
		password  = self.cleaned_data.get('password')
		password2 = self.cleaned_data.get('password2')
		if password2 != password :
			raise forms.ValidationError('passowrds dosnt matchs')
		return data

class LoginForm(forms.Form):
	username  = forms.CharField(widget=forms.TextInput(
					attrs={"class":"form-control"
					,"placeholder":"Username"}))
	password  = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"
						,"placeholder":"password"}))