from django.test import TestCase
from restaurant.models import Menu


class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="Icecream", price=2.5, inventory=80)
        self.assertEqual(str(item), "Icecream : 2.5")
