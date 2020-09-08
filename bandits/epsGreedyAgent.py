
import numpy as np
import sys
import copy
import time
import random
import argparse
######################################################

#Okay what do we need to do. First, create agents. This should use command line args. 
#Also we need to create the game
class epsGreedyAgent:
    eps = 1 #need a good value for epsilon

    def __init__(self):
        #self.currentState.print_board()
        self.name = "Eric the Epsilon Greedy Agent"
    
    def recommendArm(self, bandit, history):
        #Look at each arm
            #calculate best looking arm
            #Q_hat = 1/timesPulledCurrentArm * SUM(reward_at_time_t * (a_tau == a))
                #look at agent history to get times each arm has been pulled

            #Best looking arm is the one with the largest Q_hat
        #Calculate weighted probability of each arm 
            #if: arm is the best looking arm, then its probability = 1 - eps + eps/k
            #else: probability = eps/k
                #what is k?

        #using the weighted probabilites, generate a random number between 0 and SUM(prob_of_all_arms)
        #if random number < probability_of_arm then choose that arm
        #else keep going
        return False
