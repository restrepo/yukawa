import unittest
from yukawa import yukawa


class Test_hello(unittest.TestCase):
    def test__working(self):

        self.assertEqual(len(yukawa.remove_double_intersection_pairs(
                         [(-10, 11), (-12, 13), (11, -12)],
                         [-10, 11, -12, 13])), 2,True)
        self.assertEqual(len(yukawa.remove_double_intersection_pairs(
                         [(4,4),(4,-12)],[4,-12])),1,True)

        self.assertEqual(yukawa.get_massive_fermions([1, 3, 4, 6, -7, -8, -13, 14],7).get('S'),
                         7, True)
        self.assertEqual(yukawa.get_massive_fermions([2, 4, 4, 5, 5, 7], 9).get('S'),
                         9, True)


if __name__ == '__main__':
    unittest.main()
