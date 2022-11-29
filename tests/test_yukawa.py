import unittest
from yukawa import yukawa


class Test_hello(unittest.TestCase):
    def test__working(self):
        self.assertEqual(yukawa.get_massive_fermios([1, 3, 4, 6, -7, -8, -13, 14],7).get('s'),
                         7, True)


if __name__ == '__main__':
    unittest.main()
