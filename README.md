# barberodurmiente

Mi dirección de GitHub para este repositorio es la siguiente: [GitHub](https://github.com/lauralardies/barberodurmiente)
https://github.com/lauralardies/barberodurmiente

## Breve introducción
Este ejercicio nos presenta el problema del Barbero Durmiente y cómo resolverlo.
¿En qué consiste el **problema del Barbero Durmiente**?
El barbero sólo tiene acceso a un cliente en un momento dado, no puede atender a varios clientes a la vez. De esta manera, vamos a tener una cola que sigue un orden (gente esperando al barbero para que les corte el pelo). Mientras no hay clientes en barbero duerme, en cuanto llega un cliente el barbero se despierta.

## Código
Todos los archivos están guardados en la carpeta `barbero_durmiente`.

### Código `globals.py`
```
class Global():
    cola = [] # Lista de clientes en la sala de espera

var_global = Global()
```

### Código `barbero.py`
```
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
```

### Código `cliente.py`
```
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
```

### Código `main.py`
```
import zmq
import time
import threading
from barbero import barbero
from cliente import cliente

def main():

    context = zmq.Context()

    # Configuración del socket
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")

    # Iniciar el hilo del barbero
    hilo_barbero = threading.Thread(target=barbero)
    hilo_barbero.start()

    # Esperar un poco para que el barbero se duerma
    time.sleep(2)

    # Iniciar varios hilos de clientes
    for i in range(10):
        t = threading.Thread(target=cliente)
        t.start()
```

### Código `run.py`
```
from main import main

if __name__ == '__main__':
    main()
```
