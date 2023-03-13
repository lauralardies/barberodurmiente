import random

class Cliente():
    '''
    Creamos el objeto cliente, que consta de un ID (num_cliente) y un estado.
    '''
    def __init__(self, num_cliente, estado):
        self.num_cliente = num_cliente # Con esta variable conseguimos diferenciar a los clientes.
        self.estado = estado # Indica si este cliente está esperando o siendo atendido por el barbero.
        self.tiempo_esperado = 0 # Al comenzar el programa, el cliente todavía no ha esperado nada, se inicializa el tiempo esperado a 0 (min). Sólo aumenta si ya está con el barbero.
        self.tiempo_espera = random.randrange(5, 25) # Al inicial el programa, se asigna un tiempo de espera aleatorio entre 5 y 25 (min).
    
    def get_numcliente(self):
        '''
        Nos devuelve el número de cliente.
        '''
        return self.num_cliente
    
    def set_numcliente(self, n):
        '''
        Establecemos el número del cliente.
        '''
        self.num_cliente = n

    def get_estado(self):
        '''
        Nos devuelve el estado del cliente.
        '''
        return self.estado