from fastapi import FastAPI         # armazena as rotas, metodos, entradas esperadas, todas as infos necessarias para rodar o protocolo HTTP.
import uvicorn                      # servidor, executa servidor TCP aplicando o protocolo HTTP. usa as infos do protocolo HTTP em FastAPI para iniciar um servidor HTTP.
import os

from app.characters.entrypoint.routes.character_routes import character_route

app = FastAPI()

# Um router é um objeto que representa um grupo de rotas, ou seja, rotas são definidas nele.
# Rotas são entradas linkadas a endereços HTTP a partir de uma URL. 
# Include router inclui um dos roteadores do programa (character_route) na variável app, que instancia FastAPI.
# O FastAPI, por sua parte, é a API e nela roteadores (um grupo de rotas) são acoplados.
# FastAPI
    # Character Router
        # POST (127.0.0.1:8001/character)
        # GET (127.0.0.1:8001/character/all)
    # Location Router
        # POST (127.0.0.1:8001/location)
        # GET (127.0.0.1:8001/location/all)
        
app.include_router(character_route)

if __name__ == "__main__":          
    api_host = os.getenv("API_HOST")
    api_port = int(os.getenv("API_PORT"))

    uvicorn.run(
        app="main:app", # script name, main, + variable name that holds FastAPI
        host=api_host, 
        port=api_port, 
        reload=True, # NÃO COLOCAR ISSO EM PRODUÇÃO!
    )