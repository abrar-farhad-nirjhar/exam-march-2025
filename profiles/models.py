from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.


class Manager(BaseUserManager):
    def create_user(self, email, password, **kwargs):
        user = User(email=email,  **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **kwargs):
        user = self.create(email, password, **kwargs)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class User(AbstractBaseUser):
    USERNAME_FIELD = "email"
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, unique=True)

    REQUIRED_FIELDS = ["first_name", "last_name", "username"]

    def get_full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"
