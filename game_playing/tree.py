"""
This file contains the definition of a minimax tree.
To be used by agents to create a tree
"""

import sys
import numpy as np
import util
import math

class Node:

    def __init__(self):
        self.value = 0
        self.isMin = False
        self.valueOrigin = None
        self.action = None

class Tree:

    def __init__(self):
        self.height = 1
        self.numNodes = 1
        self.root = Node()
        
    def Minimax(self, gameState):
        self.root = self.MaxValue(gameState)
        return self.root.action

    def MaxValue(self, state):
        self.numNodes += 1
        node = Node()
        node.isMin = False
        node.value = -math.inf
        node.action = None

        if state.complete() or self.numNodes > 10000:
            node.value = state.heuristic_value()
            return node

        for move in state.getMoves():
            newState = state.clone()
            newState.move(move)
            newNode = self.MinValue(newState)
            if newNode.value > node.value:
                node.valueOrigin = newNode
                node.value = newNode.value
                node.action = move

        return node

    def MinValue(self, state):
        self.numNodes += 1
        node = Node()
        node.isMin = True
        node.value = math.inf
        node.action = None

        if state.complete() or self.numNodes > 10000:
            node.value = state.heuristic_value()
            return node

        for move in state.getMoves():
            newState = state.clone()
            newState.move(move)
            newNode = self.MinValue(newState)
            if newNode.value < node.value:
                node.valueOrigin = newNode
                node.value = newNode.value
                node.action = move

        return node
