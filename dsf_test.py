import unittest
import numpy as np
import dsf


class MyTestCase(unittest.TestCase):
    def test_one_ordered_ret_PQ(self):

        # Low ordered system (works)
        A = np.array([[0.5]])
        B = np.array([[1]])
        C = np.array([[1]])
        D = np.array([1])

        index = [0]

        p, q = dsf.ret_PQ(A, B, C, D, index)

        self.assertIsNotNone(p)
        self.assertIsNotNone(q)
        # self.assertEqual(True, False)  # add assertion here

    def test_two_ordered_ret_PQ(self):

        # Low ordered system (works maybe)
        A = np.array([[0.5, 0], [0, 0.5]])
        B = np.array([[1, 1],[1,1]])
        C = np.array([[1], [1]])
        D = np.array([[1, 1], [1, 1]])

        index = [0]

        p, q = dsf.ret_PQ(A, B, C, D, index)

        self.assertIsNotNone(p)
        self.assertIsNotNone(q)

        # self.assertEqual(True, False)  # add assertion here

    def test_three_ordered_ret_PQ(self):

        # Low ordered system (works maybe)
        A = np.array([[0.5, 0, 0], [0, 0.5, 0], [0, 0, 0.5]])
        B = np.array([[1, 1,1],[1,1,1], [1,1,1]])
        C = np.array([[1], [1], [1]])
        D = np.array([[1, 1,1], [1, 1,1], [1,1,1]])

        index = [0]

        p, q = dsf.ret_PQ(A, B, C, D, index)

        self.assertIsNotNone(p)
        self.assertIsNotNone(q)

        # self.assertEqual(True, False)  # add assertion here

    def test_four_ordered_ret_PQ(self):

        # Low ordered system (works maybe)
        A = np.array([[0.5, 0, 0, 0], [0, 0.5, 0, 0], [0, 0, 0.5, 0], [0, 0, 0, 0.5]])
        B = np.array([[1, 1,1,1],[1,1,1,1], [1,1,1,1], [1,1,1,1]])
        C = np.array([[1], [1], [1], [1]])
        D = np.array([[1, 1,1,1], [1, 1,1,1], [1,1,1,1], [1,1,1,1]])

        index = [0]

        p, q = dsf.ret_PQ(A, B, C, D, index)

        self.assertIsNotNone(p)
        self.assertIsNotNone(q)

        # self.assertEqual(True, False)  # add assertion here


    def test_five_ordered_ret_PQ(self):

        # Low ordered system (works maybe)
        A = np.array([[0.5, 0, 0, 0,0], [0, 0.5, 0, 0,0], [0, 0, 0.5, 0,0], [0, 0, 0, 0.5,0], [0, 0, 0, 0,0.5]])
        B = np.array([[1,1,1,1,1],[1,1,1,1,1], [1,1,1,1,1], [1,1,1,1,1], [1,1,1,1,1]])
        C = np.array([[1,1,1,1,1], [1,1,1,1,1], [1,1,1,1,1], [1,1,1,1,1]])
        D = np.array([[1,1,1,1,1], [1,1,1,1,1], [1,1,1,1,1], [1,1,1,1,1]])

        index = [1,2,3]

        p, q = dsf.ret_PQ(A, B, C, D, index)


        self.assertIsNotNone(p)
        self.assertIsNotNone(q)
		
        # self.assertEqual(True, False)  # add assertion here


if __name__ == "__main__":
    unittest.main()
