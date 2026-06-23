from fastapi import APIRouter
from gerador import Gerador
import requests
import json

router = APIRouter(prefix="/gerador", tags=["Gerador"])

@router.post("/")
def gerar_questoes(gerador: Gerador):

    apikey =

    tema = gerador.requisicao

    url = 'https://generativelanguage.googleapis.com/v1beta/interactions'

    headers = {
        'Content-Type': 'application/json',
        'x-goog-api-key': apikey
    }

    data = {
        "model": "gemini-3.1-flash-lite",
        "input": "Gere 5 questões em formato json sem nenhum texto adicional sobre" + tema
    }

    response = requests.post(
        url,
        headers=headers,
        data=json.dumps(data)
    )

    resultado = response.json()

    texto = resultado['steps'][1]['content'][0]['text']

    return json.loads(texto)