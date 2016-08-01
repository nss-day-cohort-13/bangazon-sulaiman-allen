import unittest
from bangazon import *


class bangTester(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.bang = Bangazon()

    def test_bangazon_class_is_of_type_bangazon(self):
        self.assertIsInstance(self.bang, Bangazon)











if __name__ == '__main__':
    unittest.main()
