import unittest
import numpy as np
import dsf

class MyTestCase(unittest.TestCase):
    def test_ret_PQ(self):
        A = np.array([[0.5, 0, 0, 0], [0, 0.5, 0, 0], [0, 0, 0.5, 0], [0, 0, 0, 0.5]])
        B = np.array([[1], [1], [1], [1]])
        C = np.array([[1, 1, 1, 1]])
        D = np.array([1])
        index = [0]

        print(index)
        print(np.arange(D.shape[0]))

        p, q = dsf.ret_PQ(A, B, C, D, index)

        print(p)
        print(q)

        self.assertIsNotNone(p)
        self.assertIsNotNone(q)
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
