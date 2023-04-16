from ..database.db import Base
from sqlalchemy import Column, Integer, String, DateTime , Float , Sequence


class Claim(Base):
    __tablename__ = 'claims'
    claim_id = Column(Integer, primary_key=True, index=True)
    member_id = Column(Integer,index=True,nullable=False)
    service_date = Column(DateTime)
    submitted_procedure = Column(String)
    quadrant = Column(String, nullable=True)
    plan_group = Column(String)
    subscriber = Column(Integer)
    provider_npi = Column(Integer)
    provider_fees = Column(Float)
    allowed_fees = Column(Float)
    member_coinsurance = Column(Float)
    member_copay = Column(Float)
    net_fee = Column(Float)
    processing_fees = Column(Float)

    def __repr__(self) -> str:
        return f'<Claim Id: {self.claim_id}>'
    


