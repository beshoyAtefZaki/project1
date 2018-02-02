# from rest_framework import generics
from profiles.models import Post
from rest_framework import serializers

class PostSerialzier(serializers.ModelSerializer):
	class Meta:
		model = Post
		fields= [
		'pk',
		'user',
		'post',
		'date',
		]
