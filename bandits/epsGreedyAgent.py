
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
    eps = 0.5 #need a good value for epsilon

    def __init__(self):
        #self.currentState.print_board()
        self.name = "Eric the Epsilon Greedy Agent"

    """
    bandit is the current bandit with variables like: arms
    history is an array with format [arm_pulled, reward]
    """
    def recommendArm(self, bandit, history):
        #Look at each arm
        #calculate best looking arm
        armRewards = []
        armProbs = []
        for arm in range(bandit.getNumArms()):
            timesArmPulled = 0
            cumRewardForArm = 0
            #look at agent history to get times each arm has been pulled
            for pull in history:
                if pull[0] == arm:
                    timesArmPulled += 1
                    cumRewardForArm += pull[1]
            #print(f'arm {arm} pulled {timesArmPulled} times for total reward of {cumRewardForArm}')
            if (timesArmPulled > 0):
                #Q_hat = 1/timesPulledCurrentArm * SUM(reward_at_time_t * (a_tau == a))
                q_hat = (1 / timesArmPulled) * cumRewardForArm
                armRewards.append((arm, q_hat))

        #Best looking arm is the one with the largest Q_hat
        if len(armRewards) > 0:
            q_max = list(map(max, zip(*armRewards)))

            #Calculate weighted probability of each arm
            k = 1.0
            probabilities = []
            for arm in range(bandit.getNumArms()):
                #if: arm is the best looking arm, then its probability = 1 - eps + eps/k
                if arm == q_max[0]:
                    probabilities.append(1-self.eps + (self.eps/k))
                #else: probability = eps/k
                else:
                    probabilities.append(self.eps/k)
                    #what is k?

            randNum = random.uniform(0, sum(probabilities))
            #print(probabilities)
            #print(f'randNum = {randNum} from range (0, {sum(probabilities)})')
            for i in range(len(probabilities)):
                #print(f'i = {i} prob = {probabilities[i]} random = {randNum}')
                if probabilities[i] > randNum:
                    #print(f'choosing {i}')
                    return i
                else:
                    randNum -= probabilities[i]
        return False
