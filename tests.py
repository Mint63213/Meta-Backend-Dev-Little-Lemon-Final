from django.test import TestCase, Client
from restaurant.models import Menu
from django.urls import reverse
from decimal import Decimal
import json

"""python manage.py test restaurant.tests.MenuModelTest"""
class MenuModelTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.menu_item = Menu.objects.create(
            name="Pasta",
            price=12.99,
            menu_item_description="Spaghetti with tomato sauce"
        )

    def test_menu_creation(self):
        self.assertIsInstance(self.menu_item, Menu)
        self.assertEqual(self.menu_item.name, "Pasta")
        self.assertEqual(self.menu_item.price, 12.99)
        self.assertEqual(self.menu_item.menu_item_description, "Spaghetti with tomato sauce")

    def test_menu_str(self):
        self.assertEqual(str(self.menu_item), "Pasta")

"""Authentication needs to be commented out in settings to run this test."""
"""python manage.py test tests.SingleMenuItemTest"""
class SingleMenuItemTest(TestCase):
    
        def setUp(self):
            self.client = Client()
            self.menu_item = Menu.objects.create(
                name="Pasta",
                price=12.99,
                menu_item_description="Spaghetti with tomato sauce"
            )
    
        def test_single_menu_item(self):
            response = self.client.get(reverse('menu-items-api', kwargs={'name': self.menu_item.name}))
            self.assertEqual(response.status_code, 200)
            self.assertEqual(self.menu_item.name, 'Pasta')
        def test_put_single_menu_item(self):
            data = {
                'name': 'Taco',
                'price': 15.99,
                'menu_item_description': 'Spicy, mexican, cheesy tacos'
            }
            response = self.client.put(reverse('menu-items-api', kwargs={'name': self.menu_item.name}),\
            data=json.dumps(data), content_type='application/json')
            self.assertEqual(response.status_code, 200)
            self.menu_item.refresh_from_db()
            #check the number of menu items in the database is equal to 2
            self.assertEqual(Menu.objects.count(), 1)
            self.assertEqual(self.menu_item.name, 'Taco')
        def test_patch_single_menu_item(self):
            data = {
                'price': 11.99
            }
            response = self.client.patch(reverse('menu-items-api', kwargs={'name': self.menu_item.name}),\
            json.dumps(data), content_type='application/json')
            self.assertEqual(response.status_code, 200)
            self.menu_item.refresh_from_db()
            self.assertEqual(self.menu_item.price, Decimal(data['price']).quantize(Decimal('0.01')))
        def test_delete_single_menu_item(self):
            response = self.client.delete(reverse('menu-items-api', kwargs={'name': self.menu_item.name}))
            self.assertEqual(response.status_code, 204)
            self.assertEqual(Menu.objects.count(), 0)




        
