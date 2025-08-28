from fastapi_sqlalchemy import db
from database.models import AlcoInfo as Alco

class AlcoholService:
    def get_alco():
        alco = db.session.query(Alco).all()
        return alco
    
    def get_alco_by_id(id: int):
        alco = db.session.query(Alco).filter(Alco.id == id).first()
        return alco