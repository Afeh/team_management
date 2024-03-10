from typing import Any
from django.contrib.auth.models import User
from django import forms
from .models import TeamMember

class TeamMemberForm(forms.ModelForm):
	class Meta:
		model = TeamMember
		fields = ['first_name', 'last_name', 'email', 'phone_number', 'role' ]

	
	def save(self, commit: bool = ...) -> Any:
		user = super().save(commit=False)# Partially save the TeamMember object without committing to the database
		username = f'{user.first_name}.{user.last_name}' # Generate a username from the first and last name
		name_user=User.objects.create_user(username=username)# Create a new Django User object with the generated username
		if user.role == "admin": # If the role is "admin", grant staff and superuser permissions
			name_user.is_staff = True
			name_user.is_superuser = True
			name_user.save()

		user.user=name_user # Assign the created User object to the TeamMember object's "user" field
		user.save()

		return user
