from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from phonenumber_field.modelfields import PhoneNumberField

class Role(models.Model):
	id = models.AutoField(primary_key=True)#Auto-increamenting primary key
	role = models.CharField(max_length=50)


class User(AbstractBaseUser):
	id = models.AutoField(primary_key=True)#Auto-increamenting primary key
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.EmailField(unique=True)

	admin = models.BooleanField(default=False)

	USERNAME_FIELD='email'


class Profile(models.Model):
	id = models.AutoField(primary_key=True)#Auto-increamenting primary key
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	phone_number = PhoneNumberField(blank=True) # Phone number using PhoneNumberField
	role = models.ForeignKey(Role, on_delete=models.CASCADE) #Role Name with Choices

	def __str__(self):
		return f"{self.user.first_name} {self.user.last_name}"#Return combination of last and first names
