from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, username, email=None, password=None):
        if not username:
            raise ValueError
        
        user = self.model(username=username, email=email)
        user.set_password(password)

        user.save(using=self._db)

        return user
    
    def create_admin(self, username, email=None, password=None):
        user = self.create_user(username, email, password)

        user.is_admin = True

        user.save(using=self._db)

        return user
    
    def create_superuser(self, username, email=None, password=None):
        user = self.create_user(username, email, password)

        user.is_superuser = True
        user.is_admin = True
        user.is_staff = True

        user.save(using=self._db)

        return user

class Users(AbstractBaseUser, PermissionsMixin): 
    username = models.CharField(_("username"), max_length=50, unique=True)
    email = models.EmailField(_("email"), max_length=254, unique=True, null=True)
    password = models.CharField(_("password"), max_length=100)
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)
    strikes = models.IntegerField(default=0)

    is_active = models.BooleanField(_("active"), default=True)
    is_staff = models.BooleanField(_("staff"), default=False)
    is_admin = models.BooleanField(_("admin/mod"), default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'

    def __str__(self):
        return self.username
