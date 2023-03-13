import os
import random
from cola import *
from cliente import *
from barbero import *

cola = Cola()
barbero = Barbero()
j = 0

print('¿Cuántas sillas hay en la tienda del barbero?')
sillas = int(input('>> ')) # Con esta variable podemos saber cuál va a ser el tope de nuestra cola.
os.system('cls')

while True:

    nuevo_cliente = random.randint(0, 1) # Dejamos que escoja el módulo random si hay clientes nuevos o no. En el caso de que nuevo_cliente = 1, significa que habrá un cliente más.

    if nuevo_cliente == 1:
        print('Ha llegado un cliente nuevo.')
        j = j + 1 # Añadimos el num de cliente.
        if cola.len_cola() < sillas: # La cola tiene hueco disponible.
            if cola.is_vacia() or not barbero.is_ocupado(): # El barbero atiende al cliente si es el primero de la cola o si está desocupado.
                cola.llegada_cliente(Cliente(j, 'Con barbero'))
                barbero.set_ocupado(True)
            else:
                for silla in range(1, sillas + 1):
                    if cola.len_cola() == silla:
                        cola.llegada_cliente(Cliente(j, 'En silla ' + str(silla + 1)))
                        break

        else: # La cola ya está llena, el cliente no cabe.
            j = j - 1 # Eliminamos el num de cliente que había llegado.
            print('¡El cliente se ha ido porque no había sillas disponibles!')