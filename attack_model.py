import numpy as np

class StateSpaceModel():
    def __init__(self, A, B, C, ignoreThreshold=100, impulseResponseTime=None):
        self.A = A
        self.B = B
        self.C = C
        self.ignoreThreshold = ignoreThreshold
        self._getSystemResponseTime(impulseResponseTime) # initialize the response time
        self.gamma = np.linalg.norm(self.impulseResponse, 1)
        self.zPeak = None
        self.yPeak = None

    def getNextTimestep(self, state, control):
        nextState = self.A @ state + self.B @ control
        observable = self.C @ state

        return nextState, observable

    def getObservable(self, state):
        return self.C @ state

    def _getSystemResponseTime(self, impulseResponseTime=None):
        if impulseResponseTime == None:
            maxIterations = 500 # take an initial guess at the max value
            impulseResponseTime = maxIterations + 1

            while impulseResponseTime > maxIterations:
                states = []
                observables = []

                # set initial conditions to 1
                state = np.ones(self.A.shape[-1])
                control = np.zeros(self.B.shape[-1])

                # unroll state across time
                for i in range(maxIterations):
                    state, observable = self.getNextTimestep(state, control)
                    states.append(state)
                    observables.append(observable)

                states = np.array(states)
                observables = np.array(observables)

                maxes = np.max(observables, axis=0)
                thresholds = maxes / self.ignoreThreshold

                mask = states > thresholds

                impulseResponseTime = np.max(np.sum(mask, axis=0))

                if impulseResponseTime == maxIterations:
                    maxIterations += 500
                    impulseResponseTime = maxIterations + 1

                self.impulseResponseTime = impulseResponseTime
                self.impulseResponse = states[:impulseResponseTime]
        else:
            self.impulseResponseTime = impulseResponseTime

            states = []

            # set initial conditions to 1
            state = np.ones(self.A.shape[-1])
            control = np.zeros(self.B.shape[-1])

            # unroll state across time
            for i in range(self.impulseResponseTime):
                state, observable = self.getNextTimestep(state, control)
                states.append(state)

            states = np.array(states)

            self.impulseResponse = states


    def _handleNones(self, initialState, numTimeSteps, rs, deltas):
        try:
            if initialState == None:
                initialState = np.zeros(self.A.shape[-1])
        except:
            pass
        try:
            if numTimeSteps == None:
                try:
                    if rs == None:
                        numTimeSteps = self.impulseResponseTime
                    else:
                        numTimeSteps = self.impulseResponseTime
                except:
                    numTimeSteps = rs.shape[0]
        except:
            pass
        try:
            if rs == None:
                rs = np.expand_dims(np.zeros((numTimeSteps,)), axis=1)
        except:
            pass
        try:
            if deltas == None:
                deltas = np.zeros((numTimeSteps))
        except:
            pass
        return initialState, numTimeSteps, rs, deltas

    def getAttackLame(self, z, delta):
        if self.zPeak == None:
            self.zPeak = z
        if abs(z) > abs(self.zPeak):
            self.zPeak = z
        return self.zPeak * delta


    def getAttack(self, z, delta):
        y = self.gamma * np.sign(z) + z

        if self.yPeak == None:
            self.yPeak = y
        if abs(y) > abs(self.yPeak):
            self.yPeak = y
        return self.yPeak * delta

    def modelSystem(self, initialState=None, numTimeSteps=None, rs=None, deltas=None):
        initialState, numTimeSteps, rs, deltas = self._handleNones(initialState, numTimeSteps, rs, deltas)
        self.yPeak = None
        self.zPeak = None

        xs = [initialState]
        zs = []
        us = []
        for index in range(1, numTimeSteps + 1):
            # calculate attack
            z = self.C @ xs[index - 1]
            #attack = y * deltas[index - 1]
            attack = self.getAttack(z, deltas[index - 1])

            # run normal system feedback with attack included
            x = xs[index - 1]
            u = rs[index - 1] + attack

            xs.append((self.A @ x) + (self.B @ u))
            zs.append(np.expand_dims(z, axis=0))
            us.append(u)
        xs = np.array(xs)[:-1]

        return xs, zs

    def _getXi(self, numTaps):

        ''' xi is the (desired) product of delta with the system output
            and is used to calculate the delta necessary to produce the
            desired unstable output '''

        taps = np.repeat(np.arange(1, numTaps + 1), self.impulseResponseTime)

        sgn = np.sign(np.squeeze(self.impulseResponse))
        signs = np.tile(np.flip(sgn), numTaps).flatten()

        xi = taps * signs
        xi = np.expand_dims(xi, axis=1)

        return xi

    def _trimOutput(self, z, xi, removeInitialOutput):
        if removeInitialOutput:
            z = z[1:]
            xi = xi[1:]
            z = np.concatenate((z, [z[-1]]), axis=0)
            xi = np.concatenate((xi, [xi[-1]]), axis=0)
        return z, xi

    def getUpperBound(self, array):

        array = np.squeeze(array)
        upperBound = np.empty_like(array)
        currentUpper = array[0]
        for i in range(array.shape[0]):
            if abs(array[i]) > abs(currentUpper):
                currentUpper = array[i]
            upperBound[i] = currentUpper
        upperBound = np.expand_dims(upperBound, axis=1)
        return upperBound


    def getDelta(self, numTaps, removeInitialOutput=True):
        '''
        generate the minimum-perturbation destabilizing attack
        '''

        # calculate the input required for the system to be unstable
        xi = self._getXi(numTaps)

        xs, z = self.modelSystem(rs=xi)
        z, xi = self._trimOutput(z, xi, removeInitialOutput) # give z and xi a haircut if requested

        # compute delta that was required in order to generate that system behavior
        y = self.gamma * np.sign(z) + z
        upperBoundedY = self.getUpperBound(y)
        delta = xi / upperBoundedY
        return delta, xi


# minimize the 1 norm of delta
# maximizing the infinity norm of z
