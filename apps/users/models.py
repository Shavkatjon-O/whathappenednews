from django.db import models
from django.contrib.auth.models import AbstractUser

from apps.common.models import BaseModel
from apps.users.managers import UserManager


class User(AbstractUser, BaseModel):
    username = None

    email = models.EmailField(unique=True)

    REQUIRED_FIELDS = []
    USERNAME_FIELD = "email"

    objects = UserManager()

    def __str__(self):
        return self.email
