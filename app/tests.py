# -*- encoding: utf-8 -*-
from django.test import TestCase
from .models import StudentRegister


class SRegister(TestCase):

    def test_saving(self):
        response = self.client.post('/', data={'first_name': 'admission number'})

        self.assertEqual(StudentRegister.objects.count(), 0)
        new_item = StudentRegister.objects.first()
        self.assertEqual(new_item.text, 'A new admission')

        self.assertIn('A new list item', response.content.decode())
        self.assertTemplateUsed(response, 'pages/register.html')

