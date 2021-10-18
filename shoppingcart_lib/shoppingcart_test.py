import unittest
import io
import sys
from shoppingcart import Cart

class TestCart(unittest.TestCase):
    def setUp(self):
        self.cart = Cart()
        self.cart.tambahProduk("mangga", 1)

        self.expectedEmpty = Cart()
        
        self.expected1Item = Cart()
        self.expected1Item.tambahProduk("mangga", 1)

        self.expected2Item = Cart()
        self.expected2Item.tambahProduk("mangga", 1)
        self.expected2Item.tambahProduk("apel", 2)

    def testTambahProduk(self):
        self.cart.tambahProduk("apel", 2)
        self.assertEqual(self.cart.getCart(), self.expected2Item.getCart())

    def testHapusProduk(self):
        self.cart.hapusProduk("mangga")
        self.assertEqual(self.cart.getCart(), self.expectedEmpty.getCart())

    def testTampilkanCart(self):
        capturedOutput = io.StringIO()                  # Create StringIO object
        sys.stdout = capturedOutput                     #  and redirect stdout.
        self.cart.tampilkanCart()
        sys.stdout = sys.__stdout__ 
        self.assertEqual(capturedOutput.getvalue(), "mangga (1)\n")

if __name__ == '__main__':
    unittest.main()
