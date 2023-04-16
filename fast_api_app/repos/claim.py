from fastapi import HTTPException  , Depends
from ..schemas.schema import ClaimModel
from ..model import models
from datetime import datetime
from ..database.db import SessionLocal , get_db
import random 

# validator
def validator(submitted_procedure, provider_npi):
    if not submitted_procedure.startswith('D'):
        raise HTTPException(status_code=400, detail='Submitted procedure should start with the letter D')
    
    if not provider_npi.isdigit() or len(provider_npi) != 10:
        raise HTTPException(status_code=400, detail='Provider NPI should be a 10-digit number')

# function to create claims
def create_claim(claim_list,db):
    for claim_obj in claim_list.claims:

        # Unpacking the dict and storing them in ClaimModel
        claim = ClaimModel(**claim_obj.dict())

        # Vaildate Data
        try:
            validator(claim.submitted_procedure,claim.provider_npi)
        except HTTPException as e:
            raise HTTPException(status_code=e.status_code, detail=e.detail)


        new_claim = compute_claim(claim,db)
        db.add(new_claim)
        db.commit()
        db.refresh(new_claim)

    return {'message':'Claims processed successfully.'}


# Function to compute  claim
def compute_claim(claim,db):
    # constant for all claims
    PROCESSING_FEE = 25
    # net fee calculation
    net_fee = ( (claim.provider_fees + claim.member_coinsurance + claim.member_copay) -  (claim.allowed_fees))

    date_time_string = claim.service_date
    serv_time_obj    = datetime.strptime(date_time_string, '%m/%d/%y %H:%M')
    unq_member_id    = generate_member_id(db)

    new_claim = models.Claim(
        member_id             = unq_member_id,
        service_date          = serv_time_obj,
        submitted_procedure   = claim.submitted_procedure,
        quadrant              = claim.quadrant,
        plan_group            = claim.plan_group,
        subscriber            = claim.subscriber,
        provider_npi          = claim.provider_npi,
        provider_fees         = claim.provider_fees,
        allowed_fees          = claim.allowed_fees,
        member_coinsurance    = claim.member_coinsurance,
        member_copay          = claim.member_copay,
        net_fee               = net_fee,
        processing_fees       = PROCESSING_FEE,
    )

    
    return new_claim


# generate random memeber id 
def generate_member_id(db):
    while True:
        member_id = random.randint(1, 10**9)
        claim_with_member_id = db.query(models.Claim).filter_by(member_id=member_id).first()
        if not claim_with_member_id:
            return member_id