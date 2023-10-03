import unittest

from tientrocap import tien_tro_cap

class TestTroCapCalculator(unittest.TestCase):

    def test1(self):
        self.assertEqual(tien_tro_cap(1000, -3, 't'), -1)   # âm
    def test2(self):
        self.assertEqual(tien_tro_cap(1000, 0, 't'), 0)  # 0% phụ thuộc
    def test3(self):
        self.assertEqual(tien_tro_cap(1000, 1, 't'), 1300)  # 30% phụ thuộc
    def test4(self):
        self.assertEqual(tien_tro_cap(1000, 2, 't'), 1500)  # 50% phụ thuộc
    def test5(self):
        self.assertEqual(tien_tro_cap(1000, 6, 't'), 1800)  # 80% phụ thuộc

    def test6(self):
        self.assertEqual(tien_tro_cap(1000, -6, 'g'), -1)   # âm
    def test7(self):
        self.assertEqual(tien_tro_cap(1000, 0, 'g'), 1300)  # 30% phụ thuộc
    def test8(self):
        self.assertEqual(tien_tro_cap(1000, 1, 'g'), 1500)  # 50% phụ thuộc
    def test9(self):
        self.assertEqual(tien_tro_cap(1000, 2, 'g'), 1800)  # 50% phụ thuộc
    def test10(self):
        self.assertEqual(tien_tro_cap(1000, 4, 'g'), 2000)  # 50% phụ thuộc

    def test11(self):
        self.assertEqual(tien_tro_cap(1000, 5, 'a'), 0)

if __name__ == "__main__":
    unittest.main()
