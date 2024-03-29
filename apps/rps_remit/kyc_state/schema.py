from datetime import date
from enum import Enum
from typing import TYPE_CHECKING, Optional

from sqlmodel import Field, Relationship, SQLModel

from record_service.main import RecordService


class CardType(str,Enum):
    RESIDENT_CARD="RESIDENT CARD"
    MY_NUMBER_CARD="MY NUMBER CARD"
    DRIVING_LICENSE="DRIVING LICENSE"

if TYPE_CHECKING:
    from apps.rps_remit.user.main import RemitUser
class KycStateBase(SQLModel):
    # team_id: Optional[int] = Field(default=None, foreign_key="team.id")
    user_id:Optional[int]=Field(default=1, foreign_key="remituser.id")
    number:str=None
    type:str=None
    front_img:str=None
    back_img:str=None
    tilted_img:str=None
    selfie_img:str=None
    state:str=None
    first_name:str=None
    last_name:str=None
    dob:date=None
    nationality:str=None
    intended_use_of_account:str=None
    mobile_number:str=None
    phone_number:str=None
    gender:str=None
    date_of_issue:str=None
    peroid_of_stay:str=None
    expire_date:str=None
    postal:str=None
    prefecture:str=None
    city:str=None
    street_address:str=None
    building_name:str=None
    expiry_date:str=None
    annual_income:str=None
    source_of_income:str=None
    tax_return:str=None
    home_contact_number:str=None
    emergency_contact_number:str=None
    

class KycStateRead(KycStateBase):
    id:Optional[int] = Field(default=None, primary_key=True) 



class KycCreate(KycStateBase):
    pass


class KycUpdate(KycStateBase):
    pass

     
from apps.rps_remit.user.schema import RemitUser, RemitUserRead

class KycState(KycStateBase, RecordService, table=True):
    id:Optional[int] = Field(default=None, primary_key=True) 
    user: Optional["RemitUser"] = Relationship(back_populates="kycstate")


