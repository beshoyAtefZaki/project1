from django.shortcuts import render ,redirect ,get_object_or_404
from django.views.generic import DetailView
from .models import Post
# Create your views here.


def add_post(request):
	if request.method =='POST':
		user = request.user
		post =  request.POST.get('new_post')
		new_post = Post()
		new_post.user= user
		new_post.post=post
		new_post.save()
		return redirect ('home')
	return redirect ('home')

def post_edit(request):
	if request.method =='POST':
		post_id= request.POST.get('post_id')
		new_post=request.POST.get('new_post')
		post = Post.objects.get(id=post_id)
		post.post= new_post
		post.save()
		return redirect ('home')
	return redirect ('home')

def post_delete(request):
	if request.method =='POST':
		post_id= request.POST.get('post_id')
		post = Post.objects.get(id=post_id)
		post.delete()
		return redirect ('home')

	return redirect ('home')


class PostEdit(DetailView):
	queryset = Post.objects.all()
	template_name= "posts/edit.html"

	def get_object(self,*args,**kwargs):
		request = self.request
		slug = self.kwargs.get('slug')
		qs = Post.objects.filter(slug=slug)
		if qs is None:
			raise Http404("Post doesn't exist !")
		return qs.first()