
import numpy as np
import sys
import copy
import time
import random
import argparse
######################################################

class thompsonAgent:
    def __init__(self):
        self.name = "Terry the Thompson Sampling Agent"
        self.prevQs = []
        self.prevArmCounts = []
        self.alphas = []
        self.betas = []

    def recommendArm(self, bandit, history):
        #initialize each arm with Beta(1,1)
        alphas = [1] * bandit.getNumArms()
        betas = [1] * bandit.getNumArms()
        armRewards = [0.0] * bandit.getNumArms()
        armPulls = [0] * bandit.getNumArms()
        #if there is no history, then we are in first iteration
        if len(history) > 0:
            #look at agent history to get times each arm has been pulled
            for arm in range(bandit.getNumArms()):
                timesArmPulled = 0
                cumRewardForArm = 0
                for pull in history:
                    if pull[0] == arm:
                        timesArmPulled += 1
                        cumRewardForArm += pull[1]
                if (timesArmPulled > 0):
                    #Q_hat = 1/timesPulledCurrentArm * SUM(reward_at_time_t * (a_tau == a))
                    q_hat = (1 / timesArmPulled) * cumRewardForArm
                    armRewards[arm] = q_hat
                    armPulls[arm] = timesArmPulled

            self.prevQs = armRewards
            self.prevArmCounts = armPulls
            alphas = self.alphas.copy()
            betas = self.betas.copy()


            #update alpha_betas based on previous reward
            last = history[len(history) -1]
            if last[1] == 1:
                alphas[last[0]] += 1
            else:
                betas[last[0]] += 1

        self.alphas = alphas
        self.betas = betas
        #sample u for all arm
        sample_u = [1.0] * bandit.getNumArms()
        maxArm = 0

        for arm in range(bandit.getNumArms()):
            sample_u[arm] = np.random.beta(alphas[arm], betas[arm])
            if sample_u[arm] > sample_u[maxArm]:
                maxArm = arm

        return maxArm

    """
    gets the Q values for every
    """
    def CalculateRegret(self, v):
        regret = 0
        for i in range(len(self.prevArmCounts)):
            regret += self.prevArmCounts[i] * (v - self.prevQs[i])
        return regret
