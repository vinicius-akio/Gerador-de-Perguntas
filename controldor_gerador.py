from fastapi import APIRouter
from gerador import Gerador
from sqlalchemy import create_engine, text
import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()
DATABASE_URL = os.getenv('DATABASE_URL')
apikey = os.getenv("GEMINI_API_KEY")

router = APIRouter(prefix="/gerador", tags=["Gerador"])

@router.post("/")
def gerar_questoes(gerador: Gerador):

    engine = create_engine(DATABASE_URL)

    try:
        with engine.begin() as con:
            sql = """
                INSERT INTO public.respostas (texto)
                VALUES ( :texto)
                  """ 
                       
            dados = {
                "texto" : gerador.requisicao
            }

            con.execute(text(sql), dados)

            engine.dispose()

    except Exception as e:
        return e

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