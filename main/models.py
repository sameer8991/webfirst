from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
#from django.urls import reverse
#from ckeditor.fields import RichTextField
# Create your models here.

class Post(models.Model):
	heading = models.CharField(max_length=200)
	content = models.TextField(max_length=2000)
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	categary = models.CharField(max_length=6000)
	#image=models.ImageField(upload_to="blog/images", blank=True)
	def __str__(self):
		return self.heading

class Comment(models.Model):
	author = models.CharField(max_length=60)
	body = models.TextField()
	created_on = models.DateTimeField(auto_now_add=True)
	post = models.ForeignKey("Post", on_delete=models.CASCADE)

