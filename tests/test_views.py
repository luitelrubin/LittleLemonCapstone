from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from django.urls import reverse


class MenuViewTest(TestCase):
    def setUp(self):
        item = Menu.objects.create(title="Icecream", price=60, inventory=100)
        item = Menu.objects.create(title="Chowmein Veg.", price=120, inventory=100)
        item = Menu.objects.create(title="Chowmein Chicken", price=150, inventory=10)

    def test_getall(self):
        items = Menu.objects.all()
        serialized_items = MenuSerializer(items, many=True)
        response = self.client.get("http://localhost:8000/restaurant/menu")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(serialized_items.data, response.data)
