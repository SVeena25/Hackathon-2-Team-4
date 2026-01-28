from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	phone = models.CharField(max_length=20, blank=True)
# Add more profile fields as needed

	def __str__(self):
		return self.user.username


class Task(models.Model):
	title = models.CharField(max_length=100)
	status = models.BooleanField(default=False)
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title