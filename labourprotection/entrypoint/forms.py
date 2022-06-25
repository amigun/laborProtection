from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as gtl
from django.db import models


class CustomAccountManager(BaseUserManager):

    def create_user(self, full_name, email, password, roles, kpp, inn, contacts, created_at):
        if not email:
            raise ValueError(gtl('Вы обязаны ввести email'))

        email = self.normalize_email(email)
        user = self.model(full_name=full_name, email=email, roles=roles, kpp=kpp,
                          inn=inn, contacts=contacts, created_at=created_at)
        user.set_password(password)
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    class Roles(models.TextChoices):
        ADMIN = 'admin', gtl('admin')
        MODER = 'moder', gtl('moder')
        USER = 'user', gtl('user')

    full_name = models.CharField(max_length=255)
    email = models.EmailField(gtl('email address'), unique=True)
    password = models.CharField(max_length=255)
    roles = models.CharField(max_length=5, choices=Roles.choices)
    kpp = models.CharField(max_length=255)
    inn = models.CharField(max_length=255)
    contacts = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)

    object = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name', 'password', 'roles', 'kpp', 'inn', 'contacts']

    def __str__(self):
        return self.email