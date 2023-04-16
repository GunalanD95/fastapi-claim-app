from fastapi import APIRouter ,  Depends  
# importing the db connection
from ..database.db import  get_db
from ..repos import claim 
from ..schemas.schema import ClaimsResponse
from sqlalchemy.orm import Session


claim_router = APIRouter(
    tags=['claim'],
)


@claim_router.post('/claim',status_code= 200)
async def process_claims(claim_list: ClaimsResponse , db: Session = Depends(get_db)):
    return claim.create_claim(claim_list,db)
