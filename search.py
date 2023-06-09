# search.py
# ---------
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


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"   
    visited = [] #already explored nodes   
    actions = [] #list of agent's actions
    fringe = util.Stack() #usage of stack data structure   
    fringe.push((problem.getStartState(), actions)) #get starting point and put it in stack and as initial action
    while fringe: #as long as the fringe is not empty
        node, action = fringe.pop() #get node and so direction taken from the stack
        if not node in visited: #if node is not visited
            visited.append(node) #visit it and mark it as visited
            if problem.isGoalState(node): #check if we reached the goal
                return action #if so return actions
            for successor in problem.getSuccessors(node): #for every successor of the node
                nextnodecoordinate, nextnodedirection, stepCost = successor #extract successor node, the action to get to it and the cost
                nextnodeactions = action + [nextnodedirection]
                fringe.push((nextnodecoordinate, nextnodeactions))
    return []

def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    visited = []
    actions = []  
    fringe = util.Queue() #using queue to explore all nodes at fixed step   
    fringe.push((problem.getStartState(), actions))
    while fringe:
        node, action = fringe.pop()
        if not node in visited:
            visited.append(node)
            if problem.isGoalState(node):
                return action
            for successor in problem.getSuccessors(node):
                nextnodecoordinate, nextnodedirection, stepCost = successor
                nextnodeactions = action + [nextnodedirection]
                fringe.push((nextnodecoordinate, nextnodeactions))
    return []

def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"      
    
    visited = []   
    actions = []
    fringe = util.PriorityQueue() #PriorityQueue to preorder nodes by cost of actions
    fringe.push((problem.getStartState(), actions), problem) #push node into the heap with priority based on cost from 'problem'
    while fringe:
        node, action = fringe.pop() #pop of smallest item of the heap
        if not node in visited:
            visited.append(node)
            if problem.isGoalState(node):
                return action
            for successor in problem.getSuccessors(node):
                nextnodecoordinate, nextnodedirection, stepCost = successor
                nextnodeactions = action + [nextnodedirection]
                nextnodecost = problem.getCostOfActions(nextnodeactions)
                fringe.push((nextnodecoordinate, nextnodeactions), nextnodecost) #push node into the heap with priority based on 'nextnodecost'
    return []

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"    
    visited = []
    actions = []
    fringe = util.PriorityQueue()
    fringe.push((problem.getStartState(), actions), heuristic(problem.getStartState(), problem)) #push node into the heap with priority based on heuristic
    while fringe:
        node, action = fringe.pop()
        if not node in visited:
            visited.append(node)
            if problem.isGoalState(node):
                return action
            for successor in problem.getSuccessors(node):
                nextnodecoordinate, nextnodedirection, stepCost = successor
                nextnodeactions = action + [nextnodedirection]
                nextnodecost = problem.getCostOfActions(nextnodeactions) + \
                               heuristic(nextnodecoordinate, problem)
                fringe.push((nextnodecoordinate, nextnodeactions), nextnodecost)
    return []

  


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
