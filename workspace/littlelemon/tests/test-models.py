from django.test import Testcase
from restaurant.models import MenuItem
class MenuTest(Testcase):
    def test_get_item(self):
     item = MenuItem.objects.create(title="IceCream", price=80, inventory=100)
     self.assertEqual(item, "IceCream : 80")

