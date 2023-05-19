import requests

# Configura los parámetros de autenticación
domain = 'camen-q'  # Cambia "example" por el dominio de tu cuenta de Freshservice
api_key = 'rSkqfcvIaeSD1uVLVunk'  # Cambia "your_api_key" por tu clave de API

# Hace una solicitud GET para obtener los datos de la encuesta de satisfacción
url = f'https://{domain}.freshservice.com/api/v2/surveys/satisfaction_response.json'
headers = {'Authorization': f'Basic {api_key}'}
response = requests.get(url, headers=headers)

# Verifica que la solicitud haya sido exitosa
if response.status_code != 200:
    raise ValueError('La solicitud no fue exitosa. Verifica tus credenciales y la URL.')

# Convierte la respuesta JSON en un objeto Python
data = response.json()

# Imprime los datos de la encuesta
print(data)
