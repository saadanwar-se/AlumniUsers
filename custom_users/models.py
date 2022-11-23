from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class Custom_Users(AbstractUser):
    username = models.CharField(max_length=100, null=True, blank=True, unique=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    short_intro = models.CharField(max_length=200, null=True, blank=True)
    bio = models.TextField(blank=True, null=True)
    social_github = models.CharField(max_length=200, null=True, blank=True)
    social_linkedin = models.CharField(max_length=200, null=True, blank=True)
    social_twitter = models.CharField(max_length=200, null=True, blank=True)
    social_youtube = models.CharField(max_length=200, null=True, blank=True)
    social_website = models.CharField(max_length=200, null=True, blank=True)
    choices = (
        ("ADMIN", 'ADMIN'),
        ("TEACHER", 'TEACHER'),
        ("STUDENT", 'STUDENT'),
        ("ALUMNI", 'ALUMNI')
    )
    role = models.CharField(max_length=50, choices=choices, blank=True, null=True)
    is_alumni = models.BooleanField(default=False, null=True, blank=True)
    is_teacher = models.BooleanField(default=False, null=True, blank=True)
    uuid = models.CharField(max_length=13, unique=True, editable=False, null=True, blank=True)
    company_name = models.CharField(max_length=50, null=True, blank=True)
    designation = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    custom_users = models.ForeignKey(Custom_Users, on_delete=models.CASCADE, related_name="user_post")
    picture = models.ImageField(upload_to="my_picture")
    title = models.CharField(max_length=256)
    description = models.CharField(max_length=256)


class AlumniData(models.Model):
    picture = models.ImageField(upload_to="my_picture")
    name = models.CharField(max_length=255)
    achievements = models.CharField(max_length=255)


class Announcements(models.Model):
    date = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)


class Fund_Raise(models.Model):
    custom_users = models.ForeignKey(Custom_Users, on_delete=models.CASCADE, related_name="teacher")
    title = models.CharField(max_length=256)
    description = models.CharField(max_length=256)
    amount = models.CharField(max_length=256)
    account_no = models.CharField(max_length=256)
    bank_name = models.CharField(max_length=256)
