from fastapi import FastAPI, APIRouter
from fastapi_sqlalchemy import DBSessionMiddleware
from dotenv import load_dotenv
from bar.alcohol.alcohol_controllers import alco

import uvicorn
import os


load_dotenv('.env')


app = FastAPI()
app.include_router(alco, prefix='/alcohol')
app.add_middleware(DBSessionMiddleware, db_url = os.environ['DATABASE_URL'])

if __name__ == '__main__':
    uvicorn.run(app)