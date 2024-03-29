import numpy as np
import sys
import copy
import time
import random
from randAgent import randomAgent
from epsGreedyAgent import epsGreedyAgent
from UCBAgent import UCBAgent
from thompsonAgent import thompsonAgent
import argparse
import csv
######################################################
AGENTS_MAP = {'randomAgent' : randomAgent,
               'epsGreedyAgent' : epsGreedyAgent,
              'UCBAgent': UCBAgent,
              'thompsonAgent': thompsonAgent  }

class bandit:
    def __init__(self, file):
        f = open(file, "r")
        lines = f.readlines()
        for i in range(len(lines)):
            lines[i] = lines[i].rstrip("\n")
        self.arms = []
        for i in range(1, len(lines)):
            self.arms.append(float(lines[i]))
        self.cumRegret = 0

    def pull_arm(self, arm):
        prob = self.arms[arm]

        randNum = random.random()
        if randNum <= prob:
            return 1
        else:
            return 0
    def getNumArms(self):
        return len(self.arms)

parser = argparse.ArgumentParser(description='Define bandit problem and agents.')
parser.add_argument('--input', choices=['input/test0.txt', 'input/test1.txt'], default='input/test1.txt', help='The input file, can be input/test0.txt or input/test1.txt')
parser.add_argument('--agent', choices=AGENTS_MAP.keys(), default='randomAgent', help='The bandit AI. Can be randomAgent, epsGreedyAgent, UCBAgent, or thompsonAgent')
parser.add_argument('--num_plays', type=int, default = 10000, help='The number of pulls an agent has.')
args = parser.parse_args()

testBandit = bandit(args.input)
agent = AGENTS_MAP[args.agent]()
history = []
cumulative_reward = 0

#mine
cumRegret = 0
v_star = 0
for arm in testBandit.arms:
    if arm > v_star:
        v_star = arm
#end mine
inputNum = "0"
if args.input == "input/test1.txt":
    inputNum = "1"
filename = "results/" + args.agent + "_" + inputNum + ".csv"

with open(filename, 'w', newline = '') as csvfile:
    writer = csv.writer(csvfile, delimiter = ',')
    for numRuns in range(args.num_plays):
        testArm = agent.recommendArm(testBandit, history)
        reward = testBandit.pull_arm(testArm)
        cumulative_reward += reward
        history.append((testArm, reward))
        cumRegret += (v_star - testBandit.arms[testArm])
        writer.writerow([numRuns, cumRegret])

print(cumulative_reward)
print(cumRegret)

#debug for me
pullCounts = [0] * testBandit.getNumArms()
proportionPulled = [0] * testBandit.getNumArms()
for h in history:
    pullCounts[h[0]] += 1
print(f'pull counts: {pullCounts}')
for i in range(len(proportionPulled)):
    proportionPulled[i] = pullCounts[i] / len(history)
print(f'proportion pulled: {proportionPulled}')
