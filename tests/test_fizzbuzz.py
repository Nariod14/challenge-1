import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import unittest
from src.fizzbuzz import fizzbuzz

from . import TestBase

class TestFizzbuzz(TestBase):
    # Your test methods here
    def test_fizzbuzz(self):
        self.assertEqual(fizzbuzz(15), [
            1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz",
            11, "Fizz", 13, 14, "FizzBuzz"
        ])
    
    def test_fizzbuzz0(self):
        self.assertEqual(fizzbuzz(0), [])

    def test_fizzbuzz1(self):
        self.assertEqual(fizzbuzz(1), [1])

    def test_fizzbuzz2(self):
        self.assertEqual(fizzbuzz(2), [1, 2])
    
    def test_fizzbuzz_negative(self):
        self.assertEqual(fizzbuzz(-15), [])
    pass


