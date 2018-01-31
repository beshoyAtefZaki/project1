from django.shortcuts import render ,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login ,logout ,logout
from .forms import RegisterForm ,LoginForm
from profiles.models import Post
#home page
def home (request):
	qs = Post.objects.all().order_by('date').reverse()

	content={
	'posts' : qs 
	}
	return render(request,'home.html', content)

#login page
def login_page(request):
	form = LoginForm(request.POST or None)
	content = {
	'form' : form ,
	}

	if form.is_valid():
		username = form.cleaned_data.get('username')
		password = form.cleaned_data.get('password')
		user = authenticate(username=username, password=password)
	
		if user is not None :
			login(request,user)
			content = {
						'form' : form ,

						}
			return redirect('home')
		else:
			return redirect('login')

	return render(request,'auth/login.html',content)

def register_page(request):
	form =RegisterForm(request.POST or None)
	content= {		
	'form': form
	}
	if form.is_valid():
		
		username = form.cleaned_data.get('username') 
		email    = form.cleaned_data.get('email') 
		password =  form.cleaned_data.get('password')
		new_user = User.objects.create_user(username=username,
										email=email,password=password) 
		new_user.save()
		return redirect('login')
	return render(request,'auth/register.html',content)

def log_out(request):
	logout(request)
	return redirect('login')