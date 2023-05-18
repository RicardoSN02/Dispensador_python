#
# PersistenciaBD.py
#
# Esta clase permite enviar y recibir datos de la bd del sensado del dispensador fachada
#

import datetime
from dispensadorbd import DispensadorBD

class PersistenciaBD:
    def __init__(self):

        self.__user = 'root'
        self.__password = '1234'
        self.__host = 'localhost'
        self.__database = 'dispensadorbd'
        self.__nomTablaDispensador = 'dispensador'

        self.__registroDispensador = DispensadorBD(self.__user, self.__password,self.__host, 
                                           self.__database, self.__nomTablaDispensador)


    def agregaRegistroDispensador(self, dispensador):
        ''' Agrega el registro 

            @param registro a agregar
        '''
        self.__registroDispensador.agrega(dispensador)

    def consultaRegistrosDispensador(self):
        ''' Regresa la lista de todos los registros del dispensador

            @returns La lista de todos los registros
        '''
        return self.__registroDispensador.lista()