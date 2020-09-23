import numpy as np
import sys
import copy
import time
import random
import argparse
import tree
######################################################
"""
RESULTS:
Connect4: 73 / 100 Wins against Randy the Random Agent
Breakthrough:
"""
class minMaxAgent:
    def __init__(self):
        self.name = "Manny the MinMaxAgent"

    def suggestMove(self, gameState):
        t = tree.Tree(gameState)
        root = self.MiniMaxSearch(t.root)
        node = t.root
        tabs = ""
        """
        print(f'backtracing...')
        while node != None:
            print(tabs + f'node {node.id}={node.value} from move {node.action}')
            node = node.valueOrigin
            tabs += "\t"
        """
        #print(f'suggesting {root.action}')
        return root.valueOrigin.action

    def MiniMaxSearch(self, root):
        node = self.MaxValue(root)
        return node

    def MaxValue(self, node):
        if len(node.children) == 0:
            node.value = 0
            #print(f'root reached at height: {node.height}')
            return node
        #update children
        for child in node.children:
            child = self.MinValue(child)
        #find max child
        #print(f'{node.id}={node.value} has child')
        for child in node.children:
            #print(f'\t{child.id}={child.value}')
            if child.value > node.value:
                node.value = child.value
                node.valueOrigin = child

        return node

    def MinValue(self, node):
        if len(node.children) == 0:
            node.value = node.state.heuristic_value()
            #print(f'root reached at height: {node.height}')
            return node

        for child in node.children:
            child = self.MaxValue(child)
        #print(f'{node.id}={node.value} has child')
        for child in node.children:
            #print(f'\t{child.id}={child.value}')
            if child.value < node.value:
                node.value = child.value
                node.valueOrigin = child

        return node
