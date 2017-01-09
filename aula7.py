#!/usr/bin/python3
# -*- coding: utf-8  -*-

'''
https://www.udemy.com/making-graphs-in-python-using-matplotlib-for-beginners/learn/v4/t/lecture/6304464

7. Changing the Axis Scales
'''

import matplotlib.pyplot as plt

x = []
y = []

for i in range(-10000, 10000):
    x.append(i/100)
    y.append(i/100)

plt.plot(x, y)

# linear scale
plt.xscale("linear")
plt.yscale("linear")
plt.show()

# x scale, log base 10 é o padrão
plt.plot(x, y)

# subsx é a lista de ticks between os números no gráfico plotado
plt.xscale("log", basex = 10, subsx = [2, 3, 4, 5, 6])
# plt.yscale("log", basey = 5, subsy)
plt.show()


# y scale, log base 10 é o padrão
'''
plt.plot(x, y)
plt.yscale("log")
plt.show()
'''


plt.plot(x, y)

# change the range of the linear approximation, a linha do gráfico fica mais linear
plt.xscale("symlog", basex = 5, subsx = [2, 3], linthreshx = 10)
# (-10, 10),   symetrical log

plt.show()



plt.plot(x, y)
plt.xscale("logit")
plt.show()
