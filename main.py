import uvicorn
from fastapi import FastAPI

from controldor_gerador import router as gerador_router

app = FastAPI()

app.include_router (gerador_router)

if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        port = 80,
        reload = True
    )