#!/usr/bin/env python3
# -*- coding: utf-8  -*-

'''
https://www.udemy.com/making-graphs-in-python-using-matplotlib-for-beginners/learn/v4/t/lecture/6310672

9. Dealing with Files in Python
'''

# abre o arquivo MyFile.txt para escrita
# cria o arquivo, se ele não existir na pasta

# abre ou cria o arquivo
f = open("MyFile.txt", "w")


# escreve no arquivo
f.write("Hello ")

# fecha o arquivo
f.close()


# append to it, escreve no final do arquivo
f = open("MyFile.txt", "a")
f.write("World")
f.close()


f = open("MyFile.txt", "r")
line = f.readline()
print("1 " + line)

print("2 " + line + ("\n"))

# .strip() removes all whitespace at the start and end, including spaces, tabs, newlines and carriage returns.
# igual à função trim() do PHP
# http://stackoverflow.com/questions/13013734/string-strip-in-python#13013812
print("3 " + line.strip("\n"))

# percorre a string e sempre que encontrar um espaço separa dois elementos
print(line.strip("\n").split(" "))

resultado = line.strip("\n").split(" ")  # gera uma lista
print("O método .split gera uma %s " %type(resultado))

print("\n5 " + line)

f.close()


# outra forma de manipular arquivos em Python
with open("MyFile.txt", "r") as f:
    line2 = f.readline()
    print("\nUsando 'with open()' + line2")

# não precisa usar o f.close()
