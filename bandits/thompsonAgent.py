
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
        self.alphas = []
        self.betas = []

    def recommendArm(self, bandit, history):
        #initialize each arm with Beta(1,1)
        alphas = [1] * bandit.getNumArms()
        betas = [1] * bandit.getNumArms()
        armRewards = [0.0] * bandit.getNumArms()
        timesArmPulled = 0

        if (len(history) > 0):
            alphas = self.alphas.copy()
            betas = self.betas.copy()
            
            #update alpha_betas based on previous reward
            last = history[len(history) -1]
            if last[1] == 1:
                alphas[last[0]] += 1
            else:
                betas[last[0]] += 1

        #sample u for all arm
        sample_u = [1.0] * bandit.getNumArms()
        maxArm = 0

        for arm in range(bandit.getNumArms()):
            sample_u[arm] = np.random.beta(alphas[arm], betas[arm])
            if sample_u[arm] > sample_u[maxArm]:
                maxArm = arm

        self.alphas = alphas
        self.betas = betas
        return maxArm
