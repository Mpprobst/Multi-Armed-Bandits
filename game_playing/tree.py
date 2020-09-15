"""
This file contains the definition of a minimax tree.
To be used by agents to create a tree
"""

import sys
import numpy as np
import util

class Node:

    def __init__(self, state, action):
        self.state = state
        if action != None:
            self.state.move(action)

        self.action = action
        self.children = []
        self.isMin = False
        self.valueOrigin = None
        self.visited = False

        self.isLeaf = state.complete()
        if self.isLeaf:
            self.value = state.result(state.player)
        else:
            self.value = None

    def updateValue(node):
        if self.isMin:
            if self.value == None or self.value < node.value:
                self.value = node.value
                self.valueOrigin = node
        else:
            if self.value == None or self.value > node.value:
                self.value = node.value
                self.valueOrigin = node

        self.visited = True

class Tree:

    def __init__(self, gameState):
        self.height = 1
        self.numNodes = 1
        self.root = Node(gameState, None)

    def BuildTree(self):
        currNode = None
        openList = util.Stack()
        openList.push(self.root)
        while not openList.isEmpty() and self.numNodes < 10000:
            currNode = openList.pop()
            currNode.visited = True
            if currNode.state.complete():
                continue

            if not currNode.visited:
                successors = gameState.getMoves()
                for move in successors:
                    node = Node(parent.state.clone(), move)
                    node.isMin = not parent.isMin
                    currNode.children.append(node)
                    self.numNodes += 1
                    openList.append(node)


#game has result(player) and heuristic_value() and getMoves()

    def SearchTree():
        

        return
