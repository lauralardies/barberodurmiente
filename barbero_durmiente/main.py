import zmq
import time
import threading
from barbero import barbero
from cliente import cliente

def main():
    global cola

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