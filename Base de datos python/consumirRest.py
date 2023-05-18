import requests

url = "http://<dirección_IP_ESP32>/getEstadoActual"

response = requests.get(url)
data = response.json()

estado = data["Estado"]
print("Estado actual:", estado)