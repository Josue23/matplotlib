#!/usr/bin/env python3
# -*- coding: utf-8  -*-

'''
https://www.udemy.com/making-graphs-in-python-using-matplotlib-for-beginners/learn/v4/t/lecture/6304432

4. Rotating Axis Ticks, Adding Text and Annotations
'''

import matplotlib.pyplot as plt

with open("Goals.txt", "r") as f:
    HomeTeamGoals = [ int(x) for x in f.readline().strip("\n").strip(" ").split(" ")]
    AwayTeamGoals = [ int(x) for x in f.readline().strip("\n").strip(" ").split(" ")]

xVariable = []
ticks = ["Game One", "Game Fifty", "Game 100"]

for i in range(len(HomeTeamGoals)):
    xVariable.append(i)

# plt.plot(xVariable, AwayTeamGoals, c = "green")
plt.plot(xVariable, AwayTeamGoals, c = "green", ls = "--") # ls, line style

# add latek to costumize the label
plt.title(r"Our first plot $\frac{1}{2}$")
# plt.show()

# plt.title("Our second plot")
plt.plot(xVariable, HomeTeamGoals, c = "red", ls = ":")
plt.xlim(0, 145)
plt.ylim(-0.5, 6)

# add latek to costumize the label
plt.xlabel(r"Game Number$_5$")
plt.ylabel(r"Goals Scored")

plt.xticks([49],["12/12/12"], rotation = 45)
plt.yticks([3],["Three Goals"], rotation = 90)

plt.text(50, 4, r"Our$^3$ Custom Text", fontsize = 8, color = "blue",
        rotation = 45)

plt.annotate("Text 2", xy = (130, 1), xytext = (65, 5),
        arrowprops = dict(facecolor = "red",shrink = 65))
plt.show()
