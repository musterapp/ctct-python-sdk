import unittest

from constantcontact import Attribute, Item

class Test_Item(unittest.TestCase):
    def test_item_init_from_dict(self):
        item = Item({'id': '123456', 'name': '+1 Steel Longsword of Meteor Strike'})

        self.assertEqual(item.get_name(), '+1 Steel Longsword of Meteor Strike')

    def test_item_fees(self):
        item = Item()

        self.assertEqual(item.get_attributes(), None)

        attribute1 = Attribute()
        attribute1.set_id('4321')
        attribute1.set_name('')
        attribute2 = Attribute()
        attribute2.set_id('1234')
        attribute2.set_name('')

        item.set_attributes([attribute1, attribute2])

        self.assertEqual(len(item.get_attributes()), 2)

        item.delete_attribute_by_id('1234')

        self.assertEqual(len(item.get_attributes()), 1)

        item.set_attributes([attribute1, attribute2])
        item.delete_attribute(0)

        self.assertEqual(item.get_attributes()[0].get_id(), '1234')

        item.clear_attributes()

        self.assertEqual(item.get_attributes(), None)


if __name__ == '__main__':
    unittest.main()
