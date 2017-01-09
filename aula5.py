#!/usr/bin/env python3
# -*- coding: utf-8  -*-

'''
https://www.udemy.com/making-graphs-in-python-using-matplotlib-for-beginners/learn/v4/t/lecture/6304450

5. Adjusting Plot Sizes, Adding a Legend, and Saving the Plots
'''

import matplotlib.pyplot as plt

with open("Goals.txt", "r") as f:
    HomeTeamGoals = [ int(x) for x in f.readline().strip("\n").strip(" ").split(" ")]
    AwayTeamGoals = [ int(x) for x in f.readline().strip("\n").strip(" ").split(" ")]

xVariable = []
ticks = ["Game One", "Game Fifty", "Game 100"]

for i in range(len(HomeTeamGoals)):
    xVariable.append(i)

# controla o tamanho da imagem do gráfico
plt.figure(figsize = (10, 8))

# plt.plot(xVariable, AwayTeamGoals, c = "green")
plt.plot(xVariable, AwayTeamGoals, c = "green", ls = "--",
        label = "Away Team Goals") # ls, line style

# add latek to costumize the label
plt.title(r"Our first plot $\frac{1}{2}$")
# plt.show()

# plt.title("Our second plot")
plt.plot(xVariable, HomeTeamGoals, c = "red", ls = ":",
        label = "Home Team Goals")

# adicionar egendas ao gráfico
plt.legend() # "upper right", posição padrão
# plt.legend(loc = "upper left")
# plt,legend(loc = "lower left")
# plt.legend(loc = "lower right") # loc altera a posição da legenda

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

# salvar o gráfico, com todos os resultados dos comandos acima
plt.savefig("MyFirstFigure")
plt.savefig("MyFirstFigure.pdf")
plt.savefig("MyFirstFigure.svg")

plt.show()
