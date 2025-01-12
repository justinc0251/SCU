# Aster Li, Justin Chung, Jonathan Fong
# qlearningAgents.py
# ------------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


from game import *
from learningAgents import ReinforcementAgent
from featureExtractors import *
from backend import ReplayMemory

import nn
import model
import backend
import gridworld


import random,util,math
import numpy as np
import copy

class QLearningAgent(ReinforcementAgent):
    """
      Q-Learning Agent
      Functions you should fill in:
        - computeValueFromQValues
        - computeActionFromQValues
        - getQValue
        - getAction
        - update
      Instance variables you have access to
        - self.epsilon (exploration prob)
        - self.alpha (learning rate)
        - self.discount (discount rate)
      Functions you should use
        - self.getLegalActions(state)
          which returns legal actions for a state
    """
    def __init__(self, **args):
        "You can initialize Q-values here..."
        ReinforcementAgent.__init__(self, **args)
        
        # Dictionaries are used to store data values in key:value pairs.
        self.qvalues = {} # this is a dictionary that stores the q-states with associated q-values
        # the q-states are keys, and the q-values are associated values for the keys

        "*** YOUR CODE HERE ***"

    def getQValue(self, state, action):
        """
          Returns Q(state,action)
          Should return 0.0 if we have never seen a state
          or the Q node value otherwise
        """
        "*** YOUR CODE HERE ***"
        #util.raiseNotDefined()
        if (state,action) in self.qvalues: # (state,action) is the key; (s,a) is the key (s,a): 0.5
            # return the associated q-value
            test = 0 # just for testing
            return self.qvalues[(state, action)] # return q value in dictionary associated with (state, action)
        else:
            test = 0 # just for testing
            # update the dictionary self.qvalues with this unseen (s,a) and initialize its value as 0.0
            # self.qvalues[(s,a)]=0.0
            # return this q-value     
            self.qvalues[(state, action)] = 0.0 # add a new key & q value to dictionary and initialize to 0.0
            return self.qvalues[(state, action)] # return this q value (0.0)
            

    def computeValueFromQValues(self, state):
        """
          Returns max_action Q(state,action) # which is V(state)
          where the max is over legal actions.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return a value of 0.0.
        """
        "*** YOUR CODE HERE ***"
        #util.raiseNotDefined()
        legalActions = self.getLegalActions(state) # get legal actions
        if not legalActions: #return 0.0 if there are no legal actions
            return 0.0
        V = [self.getQValue(state, action) for action in legalActions] # get V(state) which = max_action Q(state,action)
        return max(V)

    def computeActionFromQValues(self, state):
        """
          Compute the best action to take in a state.  Note that if there
          are no legal actions, which is the case at the terminal state,
          you should return None.
        """
        "*** YOUR CODE HERE ***"
        #util.raiseNotDefined()
        legalActions = self.getLegalActions(state) # get legal actions
        if not legalActions: #return None if there are no legal actions
            return None
        Q = self.computeValueFromQValues(state) # compute the q value using computerValueFromQValues
        A = []
        for action in legalActions:
            if self.getQValue(state, action) == Q: # if the currect action is the best action we can take, add to A
                A.append(action)
        if A:
            return random.choice(A) # choose any of the best actions
        else:
            return None

    def getAction(self, state):
        """
          Compute the action to take in the current state.  With
          probability self.epsilon, we should take a random action and
          take the best policy action otherwise.  Note that if there are
          no legal actions, which is the case at the terminal state, you
          should choose None as the action.
          HINT: You might want to use util.flipCoin(prob)
          HINT: To pick randomly from a list, use random.choice(list)
        """
        # Pick Action
        legalActions = self.getLegalActions(state)
        action = None
        "*** YOUR CODE HERE ***"
        #util.raiseNotDefined()
        if not legalActions:
            return action
        if util.flipCoin(self.epsilon): # with a probability of epsilon, randomly choose one of the legal actions
            action = random.choice(legalActions)
        else:
            action = self.computeActionFromQValues(state) # with a probability of 1 - epsilon, choose an action using the computeActionFromQValues function
        return action

    def update(self, state, action, nextState, reward):
        """
          The parent class calls this to observe a
          state = action => nextState and reward transition.
          You should do your Q-Value update here
          NOTE: You should never call this function,
          it will be called on your behalf
        """
        "*** YOUR CODE HERE ***"
        #util.raiseNotDefined()
        maxQ = self.computeValueFromQValues(nextState)
        sample = reward + self.discount * maxQ # compute sample
        prevQ = self.getQValue(state, action)
        newQ = (1 - self.alpha) * prevQ + self.alpha * sample # compute using the q value update equation
        # self.qvalues[(state,action)] = ...
        self.qvalues[(state,action)] = newQ # update dictionary with new (state, action) associated with q value

    def getPolicy(self, state):
        return self.computeActionFromQValues(state)

    def getValue(self, state):
        return self.computeValueFromQValues(state)


class PacmanQAgent(QLearningAgent):
    "Exactly the same as QLearningAgent, but with different default parameters"

    def __init__(self, epsilon=0.05,gamma=0.8,alpha=0.2, numTraining=0, **args):
        """
        These default parameters can be changed from the pacman.py command line.
        For example, to change the exploration rate, try:
            python pacman.py -p PacmanQLearningAgent -a epsilon=0.1
        alpha    - learning rate
        epsilon  - exploration rate
        gamma    - discount factor
        numTraining - number of training episodes, i.e. no learning after these many episodes
        """
        args['epsilon'] = epsilon
        args['gamma'] = gamma
        args['alpha'] = alpha
        args['numTraining'] = numTraining
        self.index = 0  # This is always Pacman
        QLearningAgent.__init__(self, **args)

    def getAction(self, state):
        """
        Simply calls the getAction method of QLearningAgent and then
        informs parent of action for Pacman.  Do not change or remove this
        method.
        """
        action = QLearningAgent.getAction(self,state)
        self.doAction(state,action)
        return action

class ApproximateQAgent(PacmanQAgent):
    """
       ApproximateQLearningAgent
       You should only have to overwrite getQValue
       and update.  All other QLearningAgent functions
       should work as is.
    """
    def __init__(self, extractor='IdentityExtractor', **args):
        self.featExtractor = util.lookup(extractor, globals())()
        PacmanQAgent.__init__(self, **args)
        self.weights = util.Counter()

    def getWeights(self):
        return self.weights

    def getQValue(self, state, action):
        """
          Should return Q(state,action) = w * featureVector
          where * is the dotProduct operator
        """
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

    def update(self, state, action, nextState, reward):
        """
           Should update your weights based on transition
        """
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

    def final(self, state):
        """Called at the end of each game."""
        # call the super-class final method
        PacmanQAgent.final(self, state)

        # did we finish training?
        if self.episodesSoFar == self.numTraining:
            # you might want to print your weights here for debugging
            "*** YOUR CODE HERE ***"
            pass
