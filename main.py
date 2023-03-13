import os
import random
from cola import *
from cliente import *
from barbero import *

print('¿Cuántas sillas hay en la tienda del barbero?')
sillas = input('>> ')
os.system('cls')

nuevo_cliente = random.randint(0, 1) # Dejamos que escoja el módulo random si hay clientes nuevos o no. En el caso de que nuevo_cliente = 1, significa que habrá un cliente más.
    