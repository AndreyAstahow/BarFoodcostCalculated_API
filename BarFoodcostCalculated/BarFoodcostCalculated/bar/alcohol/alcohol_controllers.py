from fastapi import APIRouter
from .alcohol_service import AlcoholService as AS

from database.schema import Alcohol as AlcoSchema

alco = APIRouter()

@alco.get('/get-all-alco/')
def all_alco():
    return AS.get_alco()

@alco.get('/get-alco-by-id/')
def alco_by_id(id):
    return AS.get_alco_by_id(id)

@alco.get('/get-alco-by-name/')
def alco_by_name(name):
    return AS.get_alco_by_name(name)

@alco.post('/load-alco/')
def load_alcohol(alco: AlcoSchema):
    return AS.load_alco(alco)