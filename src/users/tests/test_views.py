from django.test import TestCase, Client
from django.urls import reverse

from users.models import User


class UserTestCase(TestCase):

    def setUp(self):
        user = User.objects.create_user(username='MrTester2',email='MrTester2@gmail.com',password='BigTester15874',)
        self.user = user

    def test_signup(self):

        users = User.objects.count()
        data = {
            'username': 'MrTester',
            'email': 'MrTester@gmail.com',
            'password1': 'BigTester15874',
            'password2': 'BigTester15874'
            }
        reponse = self.client.post(reverse('users:signup'), data)
        new_users = User.objects.count()
        self.assertEqual(new_users, users + 1)
        self.assertEqual(reponse.status_code, 302)
        self.assertRedirects(reponse, reverse('users:signin'))


    def test_signin(self):

        reponse = self.client.post(reverse('users:signin'), {'username': self.user.username, 'password': 'BigTester15874'})
        self.assertEqual(reponse.status_code, 302)
        self.assertRedirects(reponse, reverse('users:profile'))

    def test_signout(self):

        c = Client()
        c.login(username=self.user.username, password='BigTester15874')
        reponse = c.get(reverse('users:signout'))
        test = c.logout()
        self.assertEqual(reponse.status_code, 302)
        self.assertRedirects(reponse, reverse('users:signin'))
