import unittest

from isbn import *

class isbnTests(unittest.TestCase):
    def setUp(self):
        self.digits10ok0 = '0596002920'
        self.digits10ok2 = ' 853-521-714-2 '
        self.digits10ok9 = '0-3162-8929-9'
        self.digits10okX = '013147149X'
        self.digits10okx = '013147149x'
        self.digits10nok = '0131471490'
        self.digits13ok0 = '9780316289290'
        self.digits13ok8 = '9788535217148' # '978-85-352-1714-8'
        self.digits13nok = '9780596100679'
        self.digits13isbn = '9791231231233'

    def testFilterDigits(self):
        self.assertEqual('1234567890123',filterDigits('1234567890123'))
        self.assertEqual('0596101392',filterDigits('\t0 596 10139-2\n'))
        self.assertEqual('013147149X',filterDigits('0-13-147149-X'))
        self.assertEqual('1234X',filterDigits('X1X2X3X4X'))

    def testIsValidISBN10(self):
        self.assertTrue(isValidISBN10(self.digits10ok0))
        self.assertTrue(isValidISBN10(self.digits10ok2))
        self.assertTrue(isValidISBN10(self.digits10ok9))
        self.assertTrue(isValidISBN10(self.digits10okX))
        self.assertTrue(isValidISBN10(self.digits10okx))
        self.assertFalse(isValidISBN10(self.digits10nok))
        self.assertFalse(isValidISBN10(self.digits13ok0))

    def testIsValidEAN(self):
        self.assertTrue(isValidEAN(self.digits13ok0))
        self.assertTrue(isValidEAN(self.digits13ok8))
        self.assertFalse(isValidEAN(self.digits13nok))
        self.assertFalse(isValidEAN(self.digits10ok0))

    def testIsValidISBN13(self):
        self.assertTrue(isValidISBN13(self.digits13ok0))
        self.assertTrue(isValidISBN13(self.digits13ok8))
        self.assertFalse(isValidISBN13(self.digits13nok))
        self.assertFalse(isValidISBN13(self.digits10ok0))
        
    def testConvertISBN13toLang(self):
        self.assertEqual('en',convertISBN13toLang('0001234567890'))
        self.assertEqual('en',convertISBN13toLang('0000000000000'))
        self.assertEqual('fr',convertISBN13toLang('0002000000000'))
        self.assertEqual('pt',convertISBN13toLang('0008500000000')) # Brazil
        self.assertEqual('pt',convertISBN13toLang('0009720000000')) # Portugal
        self.assertEqual('pt',convertISBN13toLang('0009890000000')) # Portugal
        self.assertEqual('es',convertISBN13toLang('0008400000000')) # Spain
        self.assertEqual('es',convertISBN13toLang('0009992500000')) # Paraguay
        self.assertEqual('es',convertISBN13toLang('0009995300000')) # Paraguay


if __name__ == '__main__':
    unittest.main()

