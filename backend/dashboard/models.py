from django.db import models 
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

from typing import List

class UserManager(BaseUserManager):
    def create_user(self, email: str, password: str = None) -> None:
        if not email:
            raise ValueError("Users must have an email address")
    
        user = self.model(
            email = self.normalize_email(email),
        )
        
        user.set_password(password)
        user.save(using=self._db)
        
        return user
    
    def create_superuser(self, email: str, password: str) -> None:
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        
        return user
    

class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="이메일", max_length=255, unique=True
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects: UserManager = UserManager()
    
    USERNAME_FIELD: str = "email"
    REQUIRED_FIELDS: List[str] = ["password"]
    
    def __str__(self) -> str:
        return f"{self.email}"
    
    def has_perm(self, perm, obj=None) -> bool:
        return True
    
    def has_module_perms(self, app_label) -> bool:
        return True
    
    @property
    def is_staff(self):
        return self.is_admin