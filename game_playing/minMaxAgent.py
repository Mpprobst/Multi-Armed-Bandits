
import numpy as np
import sys
import copy
import time
import random
import argparse
######################################################

class minMaxAgent:
    def __init__(self):
        self.name = "Manny the MinMaxAgent"

    def suggestMove(self, gameState):
        #gameState has 3 useful methods (from what I can tell)
            #draw, complete, and getMoves

        # need to build a tree, do we have to make our own tree structure?
        # expand the tree until a leaf is found
            # back prop and if there is an option available, extend that branch down to a leaf
            # if at root and there are no more options, or there are 10000 nodes, STOP

        # consider checking values and back propping in order to find the first win?
"QUESTION: Do we update the min max nodes when creating the tree or when searching?"
"QUESTION: How do we know where to stop? The first case where we see we can win or the most probable tree of winning?"
        # now search the tree starting at leaf
            # propogate up and compare leaf value to parent -- handle accordingly for min or max nodes
            # check children until there are no more children
            # propogate back up and repeat for the next parent's immdeiate children.

        return False
