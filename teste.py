apikey = 

import requests
import json

tema = input("")

url = 'https://generativelanguage.googleapis.com/v1beta/interactions'

headers = {
    'Content-Type': 'application/json',
    'x-goog-api-key': apikey
}

data = {
    "model": "gemini-3.1-flash-lite",
    "input": "Gere 5 questões sobre" + tema 
}

response = requests.post(
    url,
    headers = headers,
    data = json.dumps(data)
    )

resultado = response.json()

texto = resultado['stesps'][1]['content'][0]['text']

print(texto)