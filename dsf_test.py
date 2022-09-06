import unittest
import numpy as np
import dsf

class MyTestCase(unittest.TestCase):
    def test_ret_PQ(self):
        A = [[1, 2], [3, 4]]
        B = [[1, 2], [3, 4]]
        C = [[1, 2], [3, 4]]
        D = [[1, 2], [3, 4]]
        indicies = [[1]]

        [p, q] = dsf.ret_PQ(A, B, C, D, indicies)

        print(p)
        print(q)

        self.assertIsNotNone(p)
        self.assertIsNotNone(q)
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
