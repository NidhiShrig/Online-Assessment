from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    STUDENT = 'student'
    TEACHER = 'teacher'
    ADMIN = 'admin'

    ROLE_CHOICES = [
        (STUDENT, 'Student'),       
        (TEACHER, 'Teacher'),
        (ADMIN, 'Admin'),
    ]

    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default=STUDENT)     

    def __str__(self):
        return f"{self.username} ({self.role})"