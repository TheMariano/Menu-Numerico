#!/usr/bin/python
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
# Name: Menu-numérico
# version: 1.0.0
# Developer: TheMariano
# Created: 19/03/2021
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

import os, sys, time
from time import sleep as timeout
def restart_program():
        python = sys.executable
        os.execl(python, python, * sys.argv)
        curdir = os.getcwd()
os.system("clear")
print (" ███╗   ███╗███████╗███╗   ██╗██╗   ██╗     ██╗  ██╗ ")
print (" ████╗ ████║██╔════╝████╗  ██║██║   ██║     ╚██╗██╔╝ ")
print (" ██╔████╔██║█████╗  ██╔██╗ ██║██║   ██║█████╗╚███╔╝  ")
print (" ██║╚██╔╝██║██╔══╝  ██║╚██╗██║██║   ██║╚════╝██╔██╗  ")
print (" ██║ ╚═╝ ██║███████╗██║ ╚████║╚██████╔╝     ██╔╝ ██╗ ")
print (" ╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝      ╚═╝  ╚═╝ ")
print ("Create By : TheMariano")
print
print ("           [1]> 1 - Escolha             ")
print ("           [2]> 2 - Escolha              ")
print ("           [3]> 3 - Escolha         ")
print ("           [4]> 4 - Escolha    ")
print 
print (" [0]> Exit ")
print
A = input("Option ==>> ")

if A == "1" or A == "01":
  print ("1 - Escolha") #Aqui eu estou definindo pra ele printa na tela mais você pode por qualquer coisa aqui

elif A == "2" or A == "02":
    print ("2 - Escolha") #Aqui eu estou definindo pra ele printa na tela mais você pode por qualquer coisa aqui

elif A == "3" or A == "03":
    print ("3 - Escolha") #Aqui eu estou definindo pra ele printa na tela mais você pode por qualquer coisa aqui

elif A == "4" or A == "04":
    print ("4 - Escolha") #Aqui eu estou definindo pra ele printa na tela mais você pode por qualquer coisa aqui
    
elif A == "0" or A == "00":
    sys.exit() #Aqui é para fechar o arquivo
    
else:
     print ("\nERROR: Wrong Input")
     timeout(3)
     restart_program()
