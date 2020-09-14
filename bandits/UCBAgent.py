
import numpy as np
import sys
import copy
import time
import random
import argparse
import math
######################################################

#Okay what do we need to do. First, create agents. This should use command line args.
#Also we need to create the game
class UCBAgent:
    def __init__(self):
        #self.currentState.print_board()
        self.name = "Uma the UCB Agent"
        self.prevQs = []
        self.prevArmCounts = []

    def recommendArm(self, bandit, history):
        armRewards = [0.0] * bandit.getNumArms()
        armPulls = [0] * bandit.getNumArms()
        armProbs = [0.0] * bandit.getNumArms()
        for arm in range(bandit.getNumArms()):
            timesArmPulled = 0
            cumRewardForArm = 0
            #look at agent history to get times each arm has been pulled
            for pull in history:
                if pull[0] == arm:
                    timesArmPulled += 1
                    cumRewardForArm += pull[1]
            if timesArmPulled == 0:
                return arm
            #if history isnt larger than number of arms, then not all arms have been pulled
            elif len(history) >= bandit.getNumArms():
                #Q_hat = 1/timesPulledCurrentArm * SUM(reward_at_time_t * (a_tau == a))
                q_hat = (1 / timesArmPulled) * cumRewardForArm
                armRewards[arm] = q_hat
                armPulls[arm] = timesArmPulled

        self.prevQs = armRewards
        self.prevArmCounts = armPulls
        #Get best looking arm
        if len(armRewards) > 0:
            #Calculate weighted probability of each arm
            probabilities = [0.0] * bandit.getNumArms()
            maxArm = 0
            for arm in range(bandit.getNumArms()):
                #probability = q_hat + sqrt(-(2ln(t)) / timesArmPulled)
                probabilities[arm] = armRewards[arm] + np.sqrt(-2.0 * np.log(armPulls[arm] ** -4) / armPulls[arm])
                if probabilities[arm] > probabilities[maxArm]:
                    maxArm = arm

            return maxArm

        return False

    """
    gets the Q values for every
    """
    def CalculateRegret(self, v):
        regret = 0
        for i in range(len(self.prevArmCounts)):
            regret += self.prevArmCounts[i] * (v - self.prevQs[i])
        return regret
