from fastapi import APIRouter
from .alcohol_service import AlcoholService as AS

alco = APIRouter()

@alco.get('/get-all-alco/')
def all_alco():
    return AS.get_alco()

@alco.get('/get-alco-by-id/')
def alco_by_id(id):
    return AS.get_alco_by_id(id)