from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

ROLE_CHOICES = (
	('admin', 'Admin'),
	('regular', 'Regular'),
)


class TeamMember(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	id = models.AutoField(primary_key=True)#Auto-increamenting primary key
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.EmailField(unique=True)
	phone_number = PhoneNumberField(blank=True) # Phone number using PhoneNumberField
	role = models.CharField(max_length=50, choices=ROLE_CHOICES) #Role Name with Choices

	def __str__(self):
		return f"{self.first_name} {self.last_name}"#Return combination of last and first names
