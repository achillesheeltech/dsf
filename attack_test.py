from attack_model import *
from attack_exampleSystems import *
import matplotlib.pyplot as plt
import unittest
import numpy as np


class AttackTestCase(unittest.TestCase):
    def test_first_order_SISO(self):
        decayRates = [-0.1, -0.2, -0.5, -0.9]

        for decayRate in decayRates:

            ssm = getSISOSystem(decayRate=decayRate, impulseResponseTime=100)
            numTaps = 50
            deltas, xi = ssm.getDelta(numTaps=numTaps)

            srt = ssm.impulseResponseTime

            initialState = np.ones(ssm.A.shape[-1])
            numTimeSteps = numTaps * srt
            xs, ys = ssm.modelSystem(
                initialState=initialState, numTimeSteps=numTimeSteps, deltas=deltas
            )

            maxVal = np.max(xs)

            self.assertTrue(maxVal > 20)

    def test_second_order_SISO(self):
        pass


if __name__ == "__main__":
    unittest.main()
