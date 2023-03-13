class Cola():
    '''
    Representa una cola para atender a los clientes conforme van llegando y saliendo.
    '''
    def __init__(self):
        self.items = [] # Inicializamos con la cola vacía. No hay ningún cliente esperando a ser atendido.

    def llegada_cliente(self, cliente):
        '''
        Añadimos a los clientes al final de la cola según van llegando.
        '''
        self.items.append(cliente)
    
    def is_vacia(self):
        '''
        Nos muestra si la cola de clientes está vacía o no.
        '''
        if len(self.items) == 0:
            return True
        return False
    
    def len_cola(self):
        return len(self.items)