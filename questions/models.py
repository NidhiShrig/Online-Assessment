from django.db import models
from django.contrib.auth import get_user_model


Users = get_user_model()

class Question(models.Model):
    STATUS_CHOICE = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        )
    
    question_text = models.TextField()
    option_a = models.CharField(max_length=255)
    option_b = models.CharField(max_length=255)
    option_c = models.CharField(max_length=255)
    option_d = models.CharField(max_length=255)
    correct_answer = models.CharField(max_length=1, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')])
    marks = models.IntegerField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICE, default='pending')
    created_by = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='questions')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question_text # Return first 50 characters of the question text

