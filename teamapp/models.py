from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from phonenumber_field.modelfields import PhoneNumberField


class UserManager(BaseUserManager):
    def create_user(
        self, email, first_name, last_name,
        is_active=True,
        is_staff=False, is_admin=False
    ):
        if not email:
            raise ValueError("User must provide an email")

        user: User = self.model(
            email=self.normalize_email(email)
        )
        user.active = is_active
        user.admin = is_admin
        user.staff = is_staff
        user.set_unusable_password()
        user.save(using=self._db)
        return user

    def create_staff(self, email, first_name, last_name):
        user = self.create_user(
            email=email, first_name=first_name,
            last_name=last_name, is_staff=True)
        return user

    def create_superuser(self, email, first_name, last_name):
        user = self.create_user(
            email=email, first_name=first_name,
            last_name=last_name, is_staff=True, is_admin=True)
        return user


class Role(models.Model):
    role = models.CharField(max_length=50)

    def __str__(self):
        return self.role


class User(AbstractBaseUser):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    admin = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)

    REQUIRED_FIELDS = ['first_name', 'last_name']
    USERNAME_FIELD = 'email'

    objects = UserManager()

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def __str__(self) -> str:
        return self.email

    @property
    def is_active(self) -> bool:
        return self.active

    @property
    def is_staff(self) -> bool:
        return self.staff

    @property
    def is_admin(self) -> bool:
        return self.admin


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Phone number using PhoneNumberField
    phone_number = PhoneNumberField()
    # Role Name with Choices
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    def __str__(self):
        # Return combination of last and first names
        return f"{self.user.first_name} {self.user.last_name}"
