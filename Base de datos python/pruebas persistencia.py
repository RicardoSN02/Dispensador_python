from persistenciaBD import PersistenciaBD
from persistenciaException import PersistenciaException
from dispensadorbd import DispensadorBD
from dispensador import Dispensador
import datetime


persistencia = PersistenciaBD()

#prueba agregar
dispensador1 = Dispensador(None,1000,datetime.datetime(2023, 1, 16),datetime.time(10,5,10))
persistencia.agregaRegistroDispensador(dispensador1)
dispensador1 = Dispensador(None,1000,datetime.datetime(2023, 1, 16),datetime.time(6,0,0))
persistencia.agregaRegistroDispensador(dispensador1)
dispensador1 = Dispensador(None,1000,datetime.datetime(2023, 1, 16),datetime.time(11,0,0))
persistencia.agregaRegistroDispensador(dispensador1)
dispensador1 = Dispensador(None,1000,datetime.datetime(2023, 1, 17),datetime.time(6,0,0))
persistencia.agregaRegistroDispensador(dispensador1)
dispensador1 = Dispensador(None,1000,datetime.datetime(2023, 1, 17),datetime.time(12,0,0))
persistencia.agregaRegistroDispensador(dispensador1)
dispensador1 = Dispensador(None,1000,datetime.datetime(2023, 1, 17),datetime.time(18,10,10))
persistencia.agregaRegistroDispensador(dispensador1)
dispensador1 = Dispensador(None,1000,datetime.datetime(2023, 1, 18),datetime.time(6,0,0))
persistencia.agregaRegistroDispensador(dispensador1)
dispensador1 = Dispensador(None,1000,datetime.datetime(2023, 1, 18),datetime.time(12,0,0))
persistencia.agregaRegistroDispensador(dispensador1)
dispensador1 = Dispensador(None,1000,datetime.datetime(2023, 1, 18),datetime.time(18,10,10))
persistencia.agregaRegistroDispensador(dispensador1)







#prueba listar
lista = persistencia.consultaRegistrosDispensador()

for x in lista:
    print(x)