"""
Tests executed on the exercices.py file.
You should not code in this file unless you know what you are doing.
"""
import unittest
from exercices import *

class MyTestCase(unittest.TestCase):
    """ Unit tests for exercices file. """

    def test_htc_to_ttc(self):
        """ Basic test. Given a value, the method calculates it's taxed value. """
        self.assertEqual(12.06, htc_to_ttc(10))

    def test_htc_to_ttc_with_discount(self):
        """ Given a value, and a discount rate, the method calculates it's taxed value. """
        self.assertEqual(10.85, htc_to_ttc(10, 0.1))

    def test_htc_to_ttc_with_invalid_discount(self):
        """ If incorrect parameters given. The function generates an Exception. """
        self.skipTest("Exercice 1 : Validate the to previous methods before...")
        with self.assertRaises(Exception) as e_info:
            htc_to_ttc(10, 2)
        with self.assertRaises(Exception) as e_info:
            htc_to_ttc(10, -0.2)

    @unittest.skip("Exercice 2")
    def test_divisors(self):
        """Find the prime dividers of a number. """
        self.assertEqual({3,5}, divisors(15))
        self.assertEqual({2,263}, divisors(526))

    def test_divisors_prime_number(self):
        """ Special case if number is already a prime number """
        self.skipTest("Exercice 2 : Validate the previous step...")
        self.assertEqual('PREMIER', divisors(2))
        self.assertEqual('PREMIER', divisors(97))

    def test_divisors_multiple(self):
        """ Special case, do not return duplicates """
        self.skipTest("Exercice 2 : Validate the previous step...")
        self.assertEqual({2}, divisors(4))
        self.assertEqual({3,5,7}, divisors(525))

if __name__ == '__main__':
    unittest.main()
