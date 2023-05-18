import requests
import json

url = "http://<dirección_IP_ESP32>/cambiarServir"

# Definir el nuevo estado
nuevo_estado = "REPOSO"

# Crear el cuerpo de la solicitud en formato JSON
data = {
    "reiniciaEstado": nuevo_estado
}

# Realizar la solicitud POST
response = requests.post(url, data=json.dumps(data), headers={"Content-Type": "application/json"})

# Verificar la respuesta
if response.status_code == 200:
    print("Estado cambiado exitosamente a REPOSO")
else:
    print("Error al cambiar el estado")