from fastapi import FastAPI
from .database import db 
from .model import models
from .routers import claim_routes
from .schemas import schema


app = FastAPI()


get_db = db.get_db()
models.Base.metadata.create_all(db.engine)


@app.get('/')
def home():
    return {'message': 'Hello World'}


# register all routers
app.include_router(claim_routes.claim_router)