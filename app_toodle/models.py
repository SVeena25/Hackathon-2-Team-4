from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	phone = models.CharField(max_length=20, blank=True)
	# Add more profile fields as needed

	def __str__(self):
		return self.user.username

class Service(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField()
	image = models.ImageField(upload_to='service_images/', blank=True, null=True)

	def __str__(self):
		return self.name

class Booking(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	service = models.ForeignKey(Service, on_delete=models.CASCADE)
	date = models.DateField()
	time = models.TimeField()
	created_at = models.DateTimeField(auto_now_add=True)
	modified_at = models.DateTimeField(auto_now=True)
	is_cancelled = models.BooleanField(default=False)

	def __str__(self):
		return f"{self.user.username} - {self.service.name} on {self.date} at {self.time}"
