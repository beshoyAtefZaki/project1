from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from profiles.models import Post
from .serilizers import  PostSerialzier
class BlogPost(generics.RetrieveUpdateDestroyAPIView):
	lookup_field	= 'pk'
	queryset		=  Post.objects.all()
	serializer_class = PostSerialzier