import datetime
import os
import uuid

from django.conf import settings
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


def place_image_path(instance, filename):
    """Generate file path for new place image"""
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'

    return os.path.join('uploads/place', filename)


class MyUserManager(BaseUserManager):
    def create_user(self, email, username, name, gender, password):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            gender=gender,
            name=name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, name, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            username=username,
            name=name,
            gender='male',
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=100,
        unique=True,
    )
    username = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=50)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True, null=True)
    gender = models.CharField(max_length=10, choices=(
                ('male', 'Male'),
                ('female', 'Female'),
            ),
            default='male')
    bio = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'name']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


class Places(models.Model):
    id = models.CharField(primary_key=True, max_length=200)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    country = models.CharField(max_length=100, null=True)
    address = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True, unique=True)
    website = models.URLField(max_length=100, null=True, blank=True, unique=True)
    lat = models.FloatField(max_length=100)
    lng = models.FloatField(max_length=100)
    rate = models.FloatField(default=0)
    place_pic = models.ImageField(upload_to='place_icons', null=True, blank=True)


class Comments(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    place = models.ForeignKey(Places, on_delete=models.CASCADE)
    text = models.TextField()
    time = models.DateTimeField(default=datetime.datetime.now())
    rate = models.PositiveIntegerField(default=1)


class Pictures(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    place = models.ForeignKey(Places, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to=place_image_path)
    time = models.DateTimeField(default=datetime.datetime.now())


class Follow(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)


class CheckIn(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    place = models.ForeignKey(Places, on_delete=models.CASCADE)
    time = models.DateTimeField()


class Lists(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    num_of_items = models.PositiveIntegerField(default=0)
    list_pic = models.ImageField(upload_to='place_icons', null=True, blank=True)
    created_time = models.DateTimeField()
    description = models.TextField(null=True, blank=True)


class ItemsInList(models.Model):
    list = models.ForeignKey(Lists, on_delete=models.CASCADE)
    place = models.ForeignKey(Places, on_delete=models.CASCADE)
    added_time = models.DateTimeField()


class ListsInFollow(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    list = models.ForeignKey(Lists, on_delete=models.CASCADE)
