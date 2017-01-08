#!/usr/bin/env python3
# -*- coding: utf-8  -*-

'''
https://www.udemy.com/making-graphs-in-python-using-matplotlib-for-beginners/learn/v4/t/lecture/6304426

2. Making Line and Scatter Plots
'''

import matplotlib.pyplot as plt

with open("Goals.txt", "r") as f:
    HomeTeamGoals = [ int(x) for x in f.readline().strip("\n").strip(" ").split(" ")]
    AwayTeamGoals = [ int(x) for x in f.readline().strip("\n").strip(" ").split(" ")]

xVariable = []
for i in range(len(HomeTeamGoals)):
    xVariable.append(i)

# plt.plot(xVariable, AwayTeamGoals, c = "green")
plt.scatter(xVariable, AwayTeamGoals, c = "green", s = 12)
plt.show()

plt.scatter(xVariable, HomeTeamGoals, c = "red", s = 12)
plt.xlim(0, 145)
plt.ylim(-0.5, 6)
plt.show()
