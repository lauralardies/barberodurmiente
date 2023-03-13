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