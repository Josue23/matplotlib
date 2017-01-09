#!/usr/bin/env python3
# -*- coding: utf-8  -*-

'''
https://www.udemy.com/making-graphs-in-python-using-matplotlib-for-beginners/learn/v4/t/lecture/6304460

6. Creating 1-Dimensional and 2-Dimensional Histograms
'''

import matplotlib.pyplot as plt

with open("Goals.txt", "r") as f:
    HomeTeamGoals = [ int(x) for x in f.readline().strip("\n").strip(" ").split(" ")]
    AwayTeamGoals = [ int(x) for x in f.readline().strip("\n").strip(" ").split(" ")]

TotalGoals = HomeTeamGoals + AwayTeamGoals

plt.figure(figsize = (8, 5))
plt.hist(x = (HomeTeamGoals, AwayTeamGoals, TotalGoals), bins = range(8),
        label = ["Home Team Goals", "Away Team Goals",
            "Total Goals Scored"], align = "left")

plt.legend()
plt.xlabel("Goals Scored")
plt.ylabel("Number of goals scored")
plt.show()

plt.figure(figsize = (8, 5))

plt.hist2d(x = HomeTeamGoals,
        y = AwayTeamGoals,
        bins = (range(8), range(7)))
plt.xlabel("Home Team Goals")
plt.ylabel("Away Team Goals")
plt.colorbar()
plt.show()
