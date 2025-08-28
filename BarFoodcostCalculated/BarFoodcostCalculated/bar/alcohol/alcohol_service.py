from fastapi_sqlalchemy import db

from database.models import AlcoInfo as Alco
from database.schema import Alcohol as AlcoSchema

class AlcoholService:
    def get_alco():
        alco = db.session.query(Alco).all()
        return alco
    
    def get_alco_by_id(id: int):
        alco = db.session.query(Alco).filter(Alco.id == id).first()
        return alco
    
    def get_alco_by_name(name: str):
        alco = db.session.query(Alco).filter(Alco.name == name).first()
        return alco
    
    def load_alco(alco: AlcoSchema):
        db_alco = Alco(id=alco.id, name=alco.name, volume=alco.volume, price=alco.price)
        db.session.add(db_alco)
        db.session.commit()
        return db_alco