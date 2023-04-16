from fastapi import FastAPI
from .database import db 
from .model import models
from .routers import claim_routes


app = FastAPI()


get_db = db.get_db()
models.Base.metadata.create_all(db.engine)


@app.get('/')
def home():
    return {'message': 'Check /Docs Page'}


# register all routers
app.include_router(claim_routes.claim_router)