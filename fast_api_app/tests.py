import sys
from pathlib import Path

# Add the parent directory to the path
parent_dir = str(Path(__file__).resolve().parent.parent)
sys.path.append(parent_dir)

from fastapi.testclient import TestClient
from fastapi import Depends
from sqlalchemy.orm import Session
from fast_api_app.database.db import get_db
from fast_api_app.main import app
from fast_api_app.schemas.schema import ClaimModel, ClaimsResponse

client = TestClient(app)


def test_process_claims():
    claim_list = ClaimsResponse(
        claims=[
            ClaimModel(
                submitted_procedure="D1234",
                provider_npi="1234567890",
                service_date="3/28/18 0:00",
                plan_group="ABC",
                subscriber="3730189502",
                member_group="G1234",
                billed_amount=100,
                allowed_amount=90,
                allowed_fees=85,
                provider_fees=80,
                member_coinsurance=5,
                member_copay=5,
                quadrant="NE"
            ),
            ClaimModel(
                submitted_procedure="D1235",
                provider_npi="1234567897",
                service_date="3/28/18 0:00",
                plan_group="ABC",
                subscriber="3730189502",
                member_group="G1235",
                billed_amount=100,
                allowed_amount=900,
                allowed_fees=95,
                provider_fees=70,
                member_coinsurance=5,
                member_copay=5,
                quadrant="NE"
            ),
        ]
    )

    response = client.post("/claim", json=claim_list.dict())

    assert response.status_code == 200
    assert response.json() == {"message": "Claims processed successfully."}



if __name__ == '__main__':
    test_process_claims()