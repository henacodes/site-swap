from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager, UserManager
from django.utils import timezone

'''
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


'''






class CustomUserManager(BaseUserManager):


    def create_user(self, email, username, password=None):
        if (not email):
            raise ValueError('Users must have an email address')
        
        if not username:
            raise ValueError("Users must have username")
        
        user = self.model(email=self.normalize_email(email) , username=username)
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, email, username, password=None):
        if (not email):
            raise ValueError('Users must have an email address')
        
        if not username:
            raise ValueError("Users must have username")
        
        user = self.model(email=self.normalize_email(email) , username=username)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True

        user.set_password(password)
        user.save(using=self._db)

        return user





def get_image_file_path(self, filename):
    return f'profile_images/{self.pk}/profile_image.png'



def get_default_profile_image():
    return 'defaults/profile_image.png'







class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    name = models.CharField(max_length=60)
    username = models.CharField(max_length=15, unique=True)
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    profile_image = models.ImageField(max_length=255, upload_to=get_image_file_path, null=True, blank=True, default=get_default_profile_image)
    hide_email = models.BooleanField(default=True)


    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ["username"]

    objects = CustomUserManager()

    def __str__(self) :
        return self.username
    

    
