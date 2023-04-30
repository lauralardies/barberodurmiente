import time
import threading
from globales import var_global

def cliente():
    # Número máximo de clientes que pueden esperar en la sala de espera
    max_clientes = 5

    while True:
        # Entrar en la tienda y sentarse en la sala de espera
        print("Entrando en la tienda...")
        if len(var_global.cola) < max_clientes:
            var_global.cola.append(threading.current_thread().name)
            print(f"Sentándose en la sala de espera. Hay {len(var_global.cola)} clientes esperando.")
            # Esperar a ser atendido
            while threading.current_thread().name in var_global.cola:
                time.sleep(1)
            print("Saliendo de la tienda.")
        else:
            print("La sala de espera está llena. Saliendo de la tienda.")
        time.sleep(10)