from fastapi import APIRouter
from database.clients import getClientById

routes_clients = APIRouter()


@routes_clients.get("/get/{idClient}")
def get(idClient: str):
    return getClientById(idClient)
