
import numpy as np
import sys
import copy
import time
import random
import argparse
######################################################

#Okay what do we need to do. First, create agents. This should use command line args.
#Also we need to create the game
class randomAgent:
	def __init__(self):
		#self.currentState.print_board()
		self.name = "Randy the RandomAgent"
		self.prevQs = []
		self.prevArmCounts = []

	def recommendArm(self, bandit, history):
		numArms = bandit.getNumArms()
		armRewards = [0.0] * bandit.getNumArms()
		armPulls = [0] * bandit.getNumArms()
		for arm in range(bandit.getNumArms()):
			timesArmPulled = 0
			cumRewardForArm = 0
			#look at agent history to get times each arm has been pulled
			for pull in history:
				if pull[0] == arm:
					timesArmPulled += 1
					cumRewardForArm += pull[1]

			#print(f'arm {arm} pulled {timesArmPulled} times for total reward of {cumRewardForArm}')
			armPulls[arm] = timesArmPulled
			if (timesArmPulled > 0):
				#Q_hat = 1/timesPulledCurrentArm * SUM(reward_at_time_t * (a_tau == a))
				q_hat = cumRewardForArm / timesArmPulled
				armRewards[arm] = q_hat

		self.prevQs = armRewards
		self.prevArmCounts = armPulls

		return random.choice(range(numArms))


	def CalculateRegret(self, v):
		regret = 0
		for i in range(len(self.prevArmCounts)):
			regret += self.prevArmCounts[i] * (v - self.prevQs[i])
		return regret
