import sys
sys.path.append('../kazoeru')

import main
import unittest

class TestLeft(unittest.TestCase):
    def test_left_japanese(self):
        self.assertEqual(main.left(8, '日本語'), '日本語  ')

    def test_left_japanese2(self):
        self.assertEqual(main.left(5, '日本語'), '日本語')

class TestCount(unittest.TestCase):
    def test_count_csv1_len(self):
        d = main.count('./tests/test.csv')
        self.assertEqual(len(d), 3)

    def test_count_csv1_count_all(self):
        num = 0
        d = main.count('./tests/test.csv')
        for v in d.values():
            for n in v.values():
                num += n
        self.assertEqual(num, 51)

    def test_count_csv2_len(self):
        d = main.count('./tests/test2.csv')
        self.assertEqual(len(d), 13)

    def test_count_csv2_count_all(self):
        num = 0
        d = main.count('./tests/test2.csv')
        for v in d.values():
            for n in v.values():
                num += n
        self.assertEqual(num, 302)

class TestSimpleCount(unittest.TestCase):
    def test_simple_count_csv1_len(self):
        d = main.simple_count('./tests/test.csv')
        self.assertEqual(len(d), 3)

    def test_simple_count_csv2_len(self):
        d = main.simple_count('./tests/test2.csv')
        self.assertEqual(len(d), 13)

class TestFIleCheck(unittest.TestCase):
    def test_file_check_csv1(self):
        self.assertTrue(main.file_check('./tests/test.csv'))

    def test_file_check_csv2(self):
        self.assertTrue(main.file_check('./tests/test2.csv'))

    def test_file_check_csv3(self):
        self.assertFalse(main.file_check('./tests/test3.csv'))

class TestSum(unittest.TestCase):
    def test_sum_csv1(self):
        d = main.count('./tests/test.csv')
        num = main.sum(d)
        self.assertEqual(num, 51)

    def test_sum_csv2(self):
        d = main.count('./tests/test2.csv')
        num = main.sum(d)
        self.assertEqual(num, 302)

class TestSimpleSum(unittest.TestCase):
    def test_simple_sum_csv1(self):
        d = main.simple_count('./tests/test.csv')
        num = main.simple_sum(d)
        self.assertEqual(num, 51)

    def test_simple_sum_csv2(self):
        d = main.simple_count('./tests/test2.csv')
        num = main.simple_sum(d)
        self.assertEqual(num, 302)

if __name__ == '__main__':
    unittest.main()