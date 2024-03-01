from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
# Create your models here.
class UserAccountManager(BaseUserManager):
    def create_user(self, first_name, last_name,email,password=None)):
        if not email:
            raise ValueError('user must have email address')
        email = self.normalize_email(email)
        email=email.lower()

        user=self.model(
            first_name=first_name,
            last_name=last_name,
            email=email
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, first_name, last_name, email, password=None):
        user=self.create_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password
        )
       
        user.is_staff=True
        user.is_superuser=True
        user.save(using=self._db)

        return user