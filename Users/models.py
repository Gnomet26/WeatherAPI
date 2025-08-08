from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class CustomUserManager(BaseUserManager):

    def create(self, username, first_name, last_name, password):

        user = self.model(username = username, first_name = first_name, last_name = last_name)
        user.set_password(password)
        user.save(using = self._db)
        return user


class CustomUser(AbstractBaseUser):

    username = models.CharField(max_length=150,null=False,blank=False,unique=True)
    first_name = models.CharField(max_length=150, null=False,blank=False)
    last_name = models.CharField(max_length=150, null=False,blank=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.username



