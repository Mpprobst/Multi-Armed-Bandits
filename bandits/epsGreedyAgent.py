
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
    eps = 0.5
    def __init__(self):
        #self.currentState.print_board()
        self.name = "Eric the Epsilon Greedy Agent"

    """
    bandit is the current bandit with variables like: arms
    history is an array with format [arm_pulled, reward]
    """
    def recommendArm(self, bandit, history):
        explorationProb = random.random()
        if explorationProb < self.eps:
            #explore
            return random.randint(0, bandit.getNumArms()-1)

        #else exploit
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
                q_hat = cumRewardForArm / timesArmPulled
                armRewards.append((arm, q_hat))

        #Best looking arm is the one with the largest Q_hat
        if len(armRewards) > 0:
            q_max = armRewards[0]
            for q in armRewards:
                if q[1] > q_max[1]:
                    q_max = q
            return q_max[0]

        return False
