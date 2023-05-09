from persistenciaBD import PersistenciaBD
from persistenciaException import PersistenciaException
from dispensadorbd import DispensadorBD
from dispensador import Dispensador
import datetime

#prueba agregar
dispensador1 = Dispensador(None,1000,datetime.datetime(1970, 12, 1),datetime.time(20,10,10))

persistencia = PersistenciaBD()

persistencia.agregaRegistroDispensador(dispensador1)

#prueba listar
lista = persistencia.consultaRegistrosDispensador()

for x in lista:
    print(x)