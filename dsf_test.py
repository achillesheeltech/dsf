import unittest
import numpy as np
import dsf

class MyTestCase(unittest.TestCase):
    def test_low_ordered_ret_PQ(self):

        # Low ordered system (works)
        A = np.array([[0.5]])
        B = np.array([[1]])
        C = np.array([[1]])
        D = np.array([1])

        index = [0]

        # print(index)
        print("A.shape", A.shape)
        print("B.shape", B.shape)
        print("C.shape", C.shape)
        print("D.shape", D.shape)

        p, q = dsf.ret_PQ(A, B, C, D, index)

        # print("P", p)
        # print("Q", q)

        self.assertIsNotNone(p)
        self.assertIsNotNone(q)
        # self.assertEqual(True, False)  # add assertion here

    # def test_two_ordered_ret_PQ(self):
        # A higher order system (not yet working)
        # A = np.array([[0.5, 0, 0, 0], [0, 0.5, 0, 0], [0, 0, 0.5, 0], [0, 0, 0, 0.5]])
        # B = np.array([[1], [1], [1], [1]])
        # C = np.array([[1, 1, 1, 1]])
        # D = np.array([1])
        # index = [0]


if __name__ == '__main__':
    unittest.main()
