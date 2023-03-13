class Barbero():
    '''
    Creamos el objeto barbero donde podemos consultar el estado del barbero (is_ocupado()) además de cambiarlo (set_ocupado()).
    '''
    def __init__(self):
        self.ocupado = False # Inicialmente el barbero está dormido, a la espera de clientes.

    def is_ocupado(self):
        '''
        Nos devuelve el estado del barbero: True --> Está ocupado / False --> Está libre/durmiendo.
        '''
        return self.ocupado
    
    def set_ocupado(self, estado):
        '''
        Con esta función podemos cambiar el estado de nuestro barbero. 
        '''
        self.ocupado = estado
    