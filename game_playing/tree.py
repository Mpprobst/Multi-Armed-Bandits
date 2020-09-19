"""
This file contains the definition of a minimax tree.
To be used by agents to create a tree
"""

import sys
import numpy as np
import util
import math

MAX_NODES = 10000

class Node:

    def __init__(self, isMin, state, action):
        self.isMin = isMin
        self.state = state   # gamestate
        self.action = action  # the action that resulted in this node
        self.value = -math.inf
        if isMin:
            self.value = math.inf
        self.valueOrigin = None # the node that gave this node its value
        self.children = []
        self.visited = False
        self.id = 0
        self.height = 0

class Tree:
    "check depth and times calling heuristic"
    def __init__(self, gameState):
        self.height = 1
        self.numNodes = 1
        self.root = None
        self.leaves = 0
        self.BuildGameTree(gameState)

    def BuildGameTree(self, gameState):
        self.root = Node(False, gameState, 0)
        openList = util.Stack()
        openList.push(self.root)
        currNode = None

        while not openList.isEmpty() and self.numNodes < MAX_NODES:
            currNode = openList.pop()
            moves = currNode.state.getMoves()

            if currNode.visited:
                continue
            currNode.visited = True

            if currNode.state.complete():
                if not currNode.state.draw():
                    currNode.value = currNode.state.player
                else:
                    currNode.value = 0
                continue

            for move in moves:
                self.numNodes += 1
                if self.numNodes >= MAX_NODES:
                    break

                newState = currNode.state.clone()
                newState.move(move)
                newNode = Node(currNode.isMin^1, newState, move)
                newNode.id = self.numNodes
                newNode.height = currNode.height + 1
                currNode.children.append(newNode)
                openList.push(newNode)

    def Minimax(self, gameState):
        result = self.MaxValue(gameState, self.root)
        return result.action

    def MaxValue(self, state, parent):
        self.numNodes += 1
        node = Node()
        node.isMin = False
        node.value = -math.inf
        node.action = None
        node.parent = parent

        if state.complete() or self.numNodes > 10000:
            self.leaves += 1
            node.value = state.heuristic_value()
            prevNode = node
            return node

        for move in state.getMoves():
            newState = state.clone()
            newState.move(move)
            newNode = self.MinValue(newState, node)
            if newNode.value > node.value:
                node.valueOrigin = newNode
                node.value = newNode.value
                node.action = move

        return node

    def MinValue(self, state, parent):
        self.numNodes += 1
        node = Node()
        node.isMin = True
        node.value = math.inf
        node.action = None
        node.parent = parent

        if state.complete() or self.numNodes > 10000:
            self.leaves += 1
            node.value = state.heuristic_value()^1
            prevNode = node

            return node

        for move in state.getMoves():
            newState = state.clone()
            newState.move(move)
            newNode = self.MaxValue(newState, node)
            if newNode.value < node.value:
                node.valueOrigin = newNode
                node.value = newNode.value
                node.action = move

        return node
