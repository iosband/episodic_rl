'''
A reinforcement learning agent is a mapping from history to distributions over
policies. Our agent will determine how the data gathered affects the policy
for the subsequent episode.

author: iosband@stanford.edu
'''

class Agent(object):
    '''Agents update their internal params to provide a policy.'''

    def __init__(self):
        '''params will hold the internal agent data'''
        self.params = None

    def __str__(self):
        '''String representation is just parameters'''
        print str(self.params)

    def update_params(self, ep_data):
        '''Update the parameters based upon one set of data'''
        return NotImplementedError

    def sample_policy(self):
        '''Sample a policy based upon current parameters'''
        return NotImplementedError
