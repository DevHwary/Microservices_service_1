from django import urls
from django.conf.urls import url
from django.http import response
from django.test import client
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Product


class ProductTests(APITestCase):
    def test_create_product(self):
        url = '/api/products/'
        data = {
            "title" : "Book test cases",
            "image" : "book test cases image"
            }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 1)
        self.assertEqual(Product.objects.get().title, 'Book test cases')