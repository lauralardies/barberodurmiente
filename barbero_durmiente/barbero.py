import time
from globales import var_global

def barbero():
    while True:
        # Comprobar si hay clientes esperando
        if len(var_global.cola) > 0:
            # Tomar el siguiente cliente de la sala de espera
            cliente = var_global.cola.pop(0)
            print(f"Atendiendo a {cliente}...")
            time.sleep(2)
            print(f"{cliente} ha terminado de cortarse el pelo.")
        else:
            # Si no hay clientes, el barbero se duerme
            print("No hay clientes. El barbero se duerme.")
            time.sleep(5)