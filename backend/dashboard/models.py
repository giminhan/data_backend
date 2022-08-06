from django.contrib.auth.models import PermissionsMixin, BaseUserManager
from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from django.db import models


class AdminUserCustomManager(BaseUserManager):
    def create_user(self, email: str, name: str, password: str=None) -> None:
        if not email:
            raise ValueError("Users must have an email address")
        
        user = self.model(
            email=self.normalize_email(email),
            name=name,
        )
        
        user.set_password(password)
        user.save(using=self._db)
        
        return user