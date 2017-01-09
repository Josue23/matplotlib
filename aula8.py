#!/usr/bin/env python3
# -*- coding: utf-8  -*-


'''
https://www.udemy.com/making-graphs-in-python-using-matplotlib-for-beginners/learn/v4/t/lecture/6310668

 8. Importing Libraries in Python
 '''


'''
Forma 1 de importar uma library Python

import math
n1 = 23
n2 = math.sqrt(n1)
print("Raiz quadrada de %s é %s " %(n1, n2))
'''



'''
Forma 2 de importar uma library Python

import math as m
n1 = 23
n2 = m.sqrt(n1)
print("Raiz quadrada de %s é %s " %(n1, n2))
'''


'''
Forma 3 de importar uma library Python, importa somente a função sqrt

from math import sqrt
n1 = 23
n2 = sqrt(n1)

n2 = cos(n1)  # NameError: name 'cos' is not defined

print("Raiz quadrada de %s é %s " %(n1, n2))
'''



from math import sqrt, cos, sin, pow
n1 = 239
n2 = sin(n1)

print("Seno de %s é %s " %(n1, n2))

