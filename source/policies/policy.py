'''
A reinforcement learning policy is a mapping from states to actions.

author: iosband@stanford.edu
'''

class Policy(object):

    def sample_action(self, env):
        '''
        Sample an action according to the given policy.

        Args:
            env - Environment - MDP we want to deal with

        Returns:
            action - suitable action for the MDP
        '''
        return NotImplementedError
