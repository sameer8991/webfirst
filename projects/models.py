from django.db import models

# Create your models here.
class Project(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField()
	technology = models.CharField(max_length=20)
	image=models.ImageField(upload_to="projects/images")

	def __str__(self):
		return self.title

class Message(models.Model):
	name = models.CharField(max_length=25)
	email = models.EmailField()
	message = models.TextField()

	def __str__(self):
		return self.name
