from rest_framework.test import APITestCase
from django.urls import reverse 
from rest_framework import status
from .models import User


class AccountTests(APITestCase):


    def setUp(self):
        self.admin = User.objects.create_user(username='admin', password='adminpass', role=User.ADMIN)
        self.student = User.objects.create_user(username='student', password='studentpass', role=User.STUDENT)
        self.register_url = reverse('register')
        self.login_url = reverse('token_obtain_pair')
        self.user_list_url = reverse('user-list')
        self.profile_url = reverse('profile')

    def test_register_user(self):
        data = {
            'username': 'newuser',
            'password': 'newpass123',
            'role': User.STUDENT
        }
        url = reverse('register')
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_login_user(self):
        data = {
            'username': 'student',
            'password': 'studentpass'
        }
        url = reverse('token_obtain_pair')
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)

    def test_user_list_as_admin(self):
        self.client.force_authenticate(user = self.admin)
        url = reverse('user-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_list_as_student(self):
        self.client.force_authenticate(user = self.student)
        url = reverse('user-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_profile_access(self):
        self.client.force_authenticate(user = self.student)
        url = reverse('profile')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], 'student')