import numpy as np
import sys
import copy
import time
import random
import argparse
import tree
######################################################
"QUESTION: Do we update the min max nodes when creating the tree or when searching?"
"QUESTION: How do we know where to stop? The first case where we see we can win or the most probable tree of winning?"
"Min or max, current value, what action lead to its value"
class minMaxAgent:
    def __init__(self):
        self.name = "Manny the MinMaxAgent"

    def suggestMove(self, gameState):
        t = tree.Tree()
        return t.Minimax(gameState)
