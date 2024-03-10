from django import forms
from .models import Profile, User, Role
from phonenumber_field.formfields import PhoneNumberField


class TeamMemberForm(forms.Form):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField()
    phone_number = PhoneNumberField()
    role = forms.IntegerField()
    
    instance: User = None

    def clean_role(self):
        value = self.cleaned_data.get('role')
        exists = Role.objects.filter(id=value)
        if not exists:
            raise forms.ValidationError('Selected role is not valid')
        return exists.first()

    def save(self, *args, **kwargs):
        if self.instance:
            return self.update(*args, **kwargs)
        user = User.objects.create(
            first_name=self.cleaned_data.get('first_name'),
            last_name=self.cleaned_data.get('last_name'),
            email=self.cleaned_data.get('email'),
        )
        member = Profile.objects.create(
            user=user,
            role=self.cleaned_data.get('role'),
            phone_number=self.cleaned_data.get('phone_number'),
        )
        return member

    def update(self, *args, **kwargs):
        self.instance.first_name = self.cleaned_data.get('first_name')
        self.instance.last_name = self.cleaned_data.get('last_name')
        self.instance.email = self.cleaned_data.get('email')
        self.instance.profile.role = self.cleaned_data.get('role')
        self.instance.profile.phone_number = self.cleaned_data.get(
            'phone_number')
        self.instance.save()
        self.instance.profile.save()
        return self.instance
