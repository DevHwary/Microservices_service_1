from django import urls
from django.conf.urls import url
from django.http import response
from django.test import client
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Product
import json


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


    def test_retrieve_product(self):
        product = Product.objects.create(title='Book test cases1', image='book test cases image1')
        product.save()
        # product_id = Product.objects.first().id
        url = '/api/products/{0}'.format(product.id)
        response = self.client.get(url)
        data = {
            "title" : "Book test cases1",
            "image" : "book test cases image1"
        }
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        result = json.loads(response.content)        
        self.assertEqual(result['title'], product.title)
    