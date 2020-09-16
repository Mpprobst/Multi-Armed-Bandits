import numpy as np
import sys
import copy
import time
import random
import argparse
import tree
######################################################
"RESULTS: 72 / 100 Wins against Randy the Random Agent"
class minMaxAgent:
    def __init__(self):
        self.name = "Manny the MinMaxAgent"

    def suggestMove(self, gameState):
        t = tree.Tree()
        return t.Minimax(gameState)
