import random
import numpy as np
import math

def fatorial(num): # funcão que faz o fatorial
    if num == 0:
        return 1
    else:
        return num * fatorial(num-1)

x = np.random.randint(1,11,(10)) # usa a biblioteca numpy junto com a random para gerar 10 numeros aleatorios, entre 1 e 11, a no python para 1 numero antes então para em 10
print(x)
print(list(map(fatorial,x))) #usa o map para um mapa do tipo lista, com os parametros fatorial(funcão) e x(lista dos numero aleatorios)
