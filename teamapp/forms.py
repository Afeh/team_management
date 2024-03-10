from typing import Any
from django import forms
from .models import Profile, User, Role


class TeamMemberForm(forms.Form):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=20)
    role = forms.IntegerField()

    def clean_role(self):
        value = self.cleaned_data.get('role')
        exists = Role.objects.filter(id=value)
        if not exists:
            raise forms.ValidationError('Selected role is not valid')
        return exists.first()

    def save(self, *args, **kwargs):
        user = User.objects.create(
            first_name=self.cleaned_data.get('first_name'),
            last_name=self.cleaned_data.get('last_name'),
            email=self.cleaned_data.get('email'),
        )
        member = Profile.objects.create(
            user=user,
            role=self.cleaned_data.get('role'),
            phone_number=self.cleaned_data.get('first_name'),
        )
        return member
