import sys
from pathlib import Path

# Adiciona o diretório pai ao PATH
sys.path.append(str(Path(__file__).parent))

from fastapi import FastAPI
from routes.rotas import router

app = FastAPI()
app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)