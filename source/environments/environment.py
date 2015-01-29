'''
A reinforcement learning environment is a Markov Decision Process.
We specify a reward and transition function for a given state and action.

author: iosband@stanford.edu
'''

import numpy as np

class Environment(object):
    '''Environment holds a persistent state, reward and transition function.'''

    def __init__(self, state=np.zeros(1), timestep=0, horizon=1):
        '''
        Initialize the environment.

        Args:
            state - n x 1 - np array representing state dimension n
            timestep - int - the depth into the episode
            horizon - int - total depth of the episode
        '''
        self.state = state
        self.timestep = timestep
        self.horizon = horizon

    def sample_reward(self, action):
        '''Generate a reward based on (s,a)'''
        return NotImplementedError

    def sample_transition(self, action):
        '''Sample a policy based upon current parameters'''
        return NotImplementedError
