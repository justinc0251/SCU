# Justin Chung, Jonathan Fong, Aster Li
# multiAgents.py
# --------------
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


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent

class ReflexAgent(Agent):
    """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.  You are welcome to change
    it in any way you see fit, so long as you don't touch our method
    headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {NORTH, SOUTH, WEST, EAST, STOP}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        "*** YOUR CODE HERE ***"
        return successorGameState.getScore()

def scoreEvaluationFunction(currentGameState):
    """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    def getAction(self, gameState):
        def maximizer(state, depth, agentIndex):
            legalActions = state.getLegalActions(agentIndex)
            if depth == self.depth or state.isWin() or state.isLose() or not legalActions: #check if pacman is at max. depth (terminal state) or there are no more legal actions to take
                return self.evaluationFunction(state) #return the value of the state (utility of terminal state)

            maxVal = float('-inf') #initialize with neg. inf.
            for action in legalActions: #iterates through all legal actions to find the best action to take for max
                successor = state.generateSuccessor(agentIndex, action)
                tempVal = minimizer(successor, depth, agentIndex + 1) #recursively call min value with successor state
                maxVal = max(maxVal, tempVal) #find max. value for maximizer to choose
            return maxVal

        def minimizer(state, depth, agentIndex):
            legalActions = state.getLegalActions(agentIndex)
            if depth == self.depth or state.isWin() or state.isLose() or not legalActions: #check if pacman is at max. depth (terminal state) or there are no more legal actions to take
                return self.evaluationFunction(state) #return the value of the state (utility of terminal state)

            minVal = float('inf') #initialize with pos. inf.
            if agentIndex + 1 < state.getNumAgents(): #because there are multiple ghosts, must determine which ghost is next to pick value
                nextAgent = agentIndex + 1 
            else: #if all ghosts had their turn, go back to agent 0 (pacman)
                nextAgent = 0
            for action in legalActions: #iterates through all legal actions to find the best action to take for min
                successor = state.generateSuccessor(agentIndex, action)
                tempVal = None

                if nextAgent == 0: # if agent is pacman
                    tempVal = maximizer(successor, depth + 1, nextAgent) #recursively call max value with successor state
                else: # agent is ghost
                    tempVal = minimizer(successor, depth, nextAgent) #recursively call min value with successor state

                minVal = min(minVal, tempVal) #find min. value for minimizer to choose
            return minVal

        legalActions = gameState.getLegalActions(0)  #legal actions of pacman (going first)
        bestAction = None
        maxVal = float('-inf')

        for action in legalActions: #iterate through all of pacman's actions
            successorState = gameState.generateSuccessor(0, action)
            tempVal = minimizer(successorState, 0, 1)
            if tempVal > maxVal:
                maxVal = tempVal
                bestAction = action

        return bestAction


class AlphaBetaAgent(MultiAgentSearchAgent):
    """
    Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
        Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
        Returns the expectimax action using self.depth and self.evaluationFunction

        All ghosts should be modeled as choosing uniformly at random from their
        legal moves.
        """
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

def betterEvaluationFunction(currentGameState):
    """
    Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
    evaluation function (question 5).

    DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

# Abbreviation
better = betterEvaluationFunction
