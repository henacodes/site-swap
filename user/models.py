from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.utils import timezone


class CustomUserManager(UserManager):
    def _create_user(self, email, password , **kwargs):
        if not email:
            raise ValueError("Email field should not be empty")

        email = self.normalize_email(email)

        user = self.model(email=email, **kwargs)
        user.set_password(password)

        user.save(using=self._db)

        return user
    
    def create_user(self, email=None, password=None, **kwargs):
        kwargs.setdefault("is_staff", False)
        kwargs.setdefault("is_superuser", False)

        return self._create_user(email,  password, **kwargs)
    

    def create_staff(self, email=None,  password=None, **kwargs):
        kwargs.setdefault("is_staff", True)
        kwargs.setdefault("is_superuser", False)

        return self._create_user(email,  password, **kwargs)
    
    def create_superuser(self, email=None,  password=None, **kwargs):
        kwargs.setdefault("is_staff", True)
        kwargs.setdefault("is_superuser", True)

        return self._create_user(email,  password, **kwargs)



class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    username = models.CharField(max_length=10)

    objects = CustomUserManager()


    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'


    def get_full_name(self):
        return self.name

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"


    