from persistenciaBD import PersistenciaBD
from persistenciaException import PersistenciaException
from dispensadorbd import DispensadorBD
from dispensador import Dispensador
import datetime

dispensador1 = Dispensador(1000,datetime.datetime(1970, 12, 1),datetime.time(20,10,10))

persistencia = PersistenciaBD()

persistencia.agregaRegistroDispensador(dispensador1)
