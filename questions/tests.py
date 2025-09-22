from rest_framework.test import APITestCase
from django.urls import reverse
from questions.models import Question
from django.contrib.auth import get_user_model
from rest_framework import status

User = get_user_model()

class QuestionAPITestCase(APITestCase):

    def setUp(self):
        # Create teacher and admin users
        self.teacher = User.objects.create_user(username='teacher', password='password', role='teacher')
        self.admin = User.objects.create_user(username='admin', password='password', role='admin')

        # Question payload
        self.question_data = {
            "question_text": "What is 2 + 2?",
            "option_a": "3",
            "option_b": "4",
            "option_c": "5",
            "option_d": "6",
            "correct_answer": "B",
            "marks": 5
        }

        # Get JWT token for teacher
        response = self.client.post('/api/accounts/login/', {'username': 'teacher', 'password': 'password'})
        self.teacher_token = response.data['access']

        # Get JWT token for admin
        response = self.client.post('/api/accounts/login/', {'username': 'admin', 'password': 'password'})
        self.admin_token = response.data['access']

    def test_teacher_can_create_question(self):
        # Authenticate as teacher
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.teacher_token)
        response = self.client.post(reverse('question-list'), self.question_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_admin_can_approve_question(self):
        # Teacher creates question
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.teacher_token)
        response = self.client.post(reverse('question-list'), self.question_data, format='json')
        question_id = response.data['id']

        # Admin approves question
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.admin_token)
        response = self.client.post(reverse('question-approve', args=[question_id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status'], 'approved')

    def test_teacher_cannot_approve_question(self):
        # Teacher creates question
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.teacher_token)
        response = self.client.post(reverse('question-list'), self.question_data, format='json')
        question_id = response.data['id']

        # Teacher tries to approve → should fail
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.teacher_token)
        response = self.client.post(reverse('question-approve', args=[question_id]))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
