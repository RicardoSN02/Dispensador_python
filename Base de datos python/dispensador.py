#
# dispensador.py
# objeto que representa una instancia de un registro de el proyecto dispensador de comida

import datetime
import time

class Dispensador:

    def __init__(self, cantidad = None, fecha = None, hora = None):
        
        self._cantidad = cantidad
        self._fecha = fecha
        self._hora = hora

    @property
    def id_dispensador(self):
        ''' Regresa el id del registro del dispensador 

            @returns el id del registro del dispensador
        '''
        return self._id_dispensador

    @property
    def cantidad(self):
        ''' Regresa la cantidad

            @returns Regresa la cantidad
        '''
        return self._cantidad


    @property
    def fecha(self):
        ''' Regresa la fecha

            @returns Regresa la fecha
        '''
        return self._fecha

    @property
    def hora(self):
        ''' Regresa la hora 

            @returns la hora
        '''
        return self._hora

    @id_dispensador.setter
    def id(self, id):
        ''' Establece el id al valor recibido
            
            @param id recibido
        '''        
        self._id_dispensador = id


    @cantidad.setter
    def cantidad(self, cantidad):
        ''' Establece la cantidad al valor recibido
            
            @param cantidad al valor recibido
        '''        
        self._cantidad = cantidad

    @fecha.setter
    def fecha(self, fecha):
        ''' Establece la fecha al valor recibido
            
            @param fecha recibida
        '''        
        self._fecha = fecha

    @hora.setter
    def hora(self, hora):
        ''' Establece la hora
            
            @param hora Hora en la que se dispenso
        '''        
        self._hora = hora
		

    def __eq__(self, dispensador):
        ''' Regresa true si este registro del dispensador es igual al recibido del parametro.
            La comparacion es en base al atributo id

            @param dispensador Registron con el que se compara esta instancia de dispensador

            @returns True si este registro es igual al registro recibido
                False en caso contrario. 
        '''
        return self._id_dispensador == dispensador._id_dispensador
        
    def __ne__(self, dispensador):
        ''' Regresa true si este registro del dispensador es diferent al recibido del parametro.
            La comparacion es en base al atributo id

            @returns True si este registro es disferent al registro recibido
                False en caso contrario. 
        '''
        return self._id_dispensador != dispensador._id_dispensador

    def __str__(self):
        ''' Regresa una cadena con una representacion amigable
            de una instancia de la clase

            @returns Una cadena con una representacion amigable
                de la instancia de la clase
        '''
        return (f'Dispensador({self._id_dispensador}, {self._cantidad}, {self._fecha}, {self._hora})')
		
    def __repr__(self):
        ''' Regresa una cadena con una representacion unica
            de una instancia de la clase

            @returns Una cadena con una representacion unica
                de la instancia de la clase
        '''
        return (f'Dispensador({self._id_dispensador}, {self._cantidad}, {self._fecha}, {self._hora})')

#
# Prueba sencillas: 
#        		

#dispensador1 = Dispensador('12341234',1000,datetime.datetime(1970, 12, 1),datetime.time(20,10,10))
#dispensador2 = Dispensador('76546745',1000,datetime.datetime(1970, 12, 1),datetime.time(20,10,10))
#dispensador3 = Dispensador('25725757',1000,datetime.datetime(1970, 12, 1),datetime.time(20,10,10))

#print(dispensador1)
#print(dispensador2)
#print(dispensador3)