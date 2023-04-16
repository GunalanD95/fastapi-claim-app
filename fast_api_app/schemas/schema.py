from pydantic import BaseModel 
from typing   import Optional , List
from pydantic import BaseModel 


# Claim Input Model
class ClaimModel(BaseModel):
    service_date: str
    submitted_procedure: str
    quadrant: Optional[str] = ''
    plan_group: str 
    subscriber: str 
    provider_npi: str 
    provider_fees: float 
    allowed_fees: float 
    member_coinsurance: float
    member_copay: float 
    member_id : Optional[int] = None


# List of Claim Objects 
class ClaimsResponse(BaseModel):
    claims: List[ClaimModel]
