#
# generosBD.py
#

import mysql.connector
from tabla import Tabla
from dispensador import Dispensador
from persistenciaException import PersistenciaException

class DispensadorBD(Tabla):
    
    def __init__(self, user, password, host, database, nomTablaDispensador):
        ''' Constructor de la clase. Inicializa los atributos empleados para 
            conectarse con la BD

            @param user Nombre del usuario de la base de datos
            @param password Contrasenha del usuario de la base de datos 
            @param host Dirección IP de la computadora con la base de datos
            @param database Base de datos 
            @param nomTablaDispensador Nombre de la tabla en la BD para el dispensador
        '''
        super().__init__(user, password, host, database)
        self.nomTablaDispensador = nomTablaDispensador
 

    def agrega(self, dispensador):
        ''' Agrega el registro 

            @param registro Registro a agregar
            @throws PersistenciaException 
        '''
           
        operacion = f"INSERT {self.nomTablaDispensador}"
        operacion += f" SET cantidad = '{dispensador.cantidad}'"
        operacion += f", fecha = '{dispensador.fecha}'"
        operacion += f", hora = '{dispensador.hora}';"
    
        try:
            super().actualiza(operacion)
        except mysql.connector.Error as e:
            raise PersistenciaException(f'Error: {self.msj_error(e)} en la tabla {self.nomTablaDispensador} de la base de datos {self.database}') from e
           

