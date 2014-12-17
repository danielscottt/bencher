# -*- coding: utf-8 -*-

import unittest, sys
from os import path

here = path.abspath(path.dirname(__file__))
sys.path.append(path.join(here, '../'))
import bencher

def mock_func(i):
    while i < 1024:
        i = i**2

class TestBencherMethods(unittest.TestCase):

    def setUp(self):
        self.func = mock_func
        self.bencher = bencher.Bencher(self.func)
        setattr(self.bencher, 'ops', [
            {
                'time': 1.0,
                'seq': 1
            },
            {
                'time': 2.0,
                'seq': 2
            },
            {
                'time': 3.0,
                'seq': 3
            }
        ])

    def test_avg(self):
        self.assertEqual(self.bencher.avg(), 2)

    def test_total(self):
        self.assertEqual(self.bencher.total(), '6μs')

    def test_high(self):
        self.assertEqual(self.bencher.high()['time'], 3)

    def test_low(self):
        self.assertEqual(self.bencher.low()['time'], 1)

class TestBencherCalling(unittest.TestCase):

    bencher.Bencher.limit = 10

    def setUp(self):
        self.bencher = bencher.Bencher(mock_func)

    def test_calling(self):
        self.bencher(2)

    def test_call_count(self):
        self.bencher(2)
        self.assertEqual(len(self.bencher.ops), 10)

    def test_return_value(self):
        setattr(self.bencher, '_func', lambda x,y: x+y)
        ret = self.bencher(2,2)
        self.assertEqual(ret, 4)

if __name__ == '__main__':
    unittest.main()
