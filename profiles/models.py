from django.db import models
from django.contrib.auth.models import User 
from django.db.models.signals import pre_save
from django.urls import reverse
from .utils import unique_slug_generator


class Post(models.Model):
	user 	= models.ForeignKey(User , on_delete=models.CASCADE )
	post 	= models.CharField(max_length=160 )
	date 	= models.DateTimeField(auto_now_add=True)
	slug 	= models.SlugField(blank=True , unique=True)

	def __str__(self):
		return str(self.id)

	def get_absolute_url(self):
		slug 	= self.slug
		# return f"/products/{slug}/"
		return reverse('edit',kwargs={'slug':slug})


def slug_pre_save_resever(sender,instance,*args,**kwargs):
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)
pre_save.connect(slug_pre_save_resever, sender=Post)