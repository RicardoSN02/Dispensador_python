from persistenciaBD import PersistenciaBD 
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from collections import Counter
from dispensador import Dispensador
import pandas as pd
import matplotlib.pyplot as plt
import time
import threading

while True:
    
  
  persistencia = PersistenciaBD()

  consulta = persistencia.consultaRegistrosDispensador()

  fechas = []
  contador = []

  for x in consulta:
    if(fechas.__contains__(x.fecha)):
        index = fechas.index(x.fecha)
        contador[index] += 1
    else:
        fechas.append(x.fecha)
        contador.append(1)


  # Crear los datos
  data = {'fechas': fechas,
        'cantidad de servidos': contador }

  # Crear el DataFrame
  df = pd.DataFrame(data)

  # Mostrar la tabla de datos
  print(df)

  df.update(df)

  # Graficar los datos
  df.plot(x='fechas', y=['cantidad de servidos'],
        kind='bar', rot=0)
  plt.xlabel('Dispensado por dia')
  plt.legend()
  plt.show()
  
     
