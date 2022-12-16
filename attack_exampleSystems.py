import numpy as np
from attack_model import *

def getSISOSystem(decayRate, impulseResponseTime=None):
    # define/import state space model of the system
    A = np.array([[decayRate]])
    B = np.array([[1]])
    C = np.array([1,])
    D = 0
    ssm = StateSpaceModel(A, B, C, ignoreThreshold=1000, impulseResponseTime=impulseResponseTime)
    return ssm


def getSISOSystem(decayRate, impulseResponseTime=None):
    # define/import state space model of the system
    A = np.array([[decayRate]])
    B = np.array([[1]])
    C = np.array([1,])
    D = 0
    ssm = StateSpaceModel(A, B, C, ignoreThreshold=1000, impulseResponseTime=impulseResponseTime)
    return ssm

