
from fastapi import APIRouter, Body
from db.models.attendance import  AttendanceUser, EmployeeModel,Otp,CompanyModel
from apps.attendance_system.schemas.attendance import AttendanceTodayDetailModel,Company,CompanyInvitation
from db.models.attendance import Otp
from requests import Session
from db.repository.fake_attendance import FakeAttendance
from db.session import get_db
from fastapi import Depends, HTTPException, Request,status,UploadFile,Form,File
from db.repository.attendance_repo import AttendanceRepo
from apps.attendance_system.route_login import get_current_user_from_token,get_current_user_from_bearer
from pydantic import BaseModel,root_validator
from typing import Optional
from schemas.attendance import AttendanceStatus, Status, StatusOut
from datetime import date, datetime, time, timedelta
from upload_file import firebase_upload
import json
import os
# 9800000000
# 1117
router =APIRouter(include_in_schema=True,prefix='/api/v1' )
class Invitations(BaseModel):
    id:int
    company:Company 
    is_accepted:bool
    is_invited:bool
    status:Status=None
    class Config:
        orm_mode=True

        
class EmployeeCompanies(BaseModel):
    invitations:list[Invitations]
    active:list[Invitations]
    inactive:list[Invitations]
    class Config:
        orm_mode=True   

class Profile(BaseModel):
    name:Optional[str] 
    email:Optional[str]
    dob:Optional[str]
    @classmethod
    def __get_validators__(cls) :
        print(cls)
        yield cls.validate_to_json

    @classmethod
    def validate_to_json(cls,value): 
        if isinstance(value,str):
            print(cls)
            return cls(**json.loads(value))
        return value   
    class Config:
        orm_mode=True

class Breaks(BaseModel):
    id:int
    break_start:time
    break_end:Optional[time]
    class Config:
        orm_mode=True
class Employee(BaseModel):
    salary:Optional[float]
    name:Optional[str]
    duty_time:Optional[time]
    class Config:
        orm_mode=True
class MissingAttendance(BaseModel):
    attendance_date=date
    start_time:time
    end_time:time
    company_id:int
    attendance_type: AttendanceStatus
#     class Config():  #to convert non dict obj to json
#         schema_extra = {
#             "example":{
#   "start_time": "string",
#   "end_time": "string",
#   "company_id": 0,
#   "attendance_type": "LATE"
# }
#         }
class CreateAttendance(BaseModel):
    id:int
    attendance_date:date
    employee_id:Optional[int]
    company_id:Optional[int]
    login_time:time=None
    logout_time:time=None
    breaks:list[Breaks]=[]
    # employee:Employee
    is_approver:bool=False
    salary:Optional[float]
    name:Optional[str]
    duty_time:Optional[time]
    class Config:
        orm_mode=True

class ResponseAttendance(BaseModel):
    id:int
    attendance_date:date
    employee_id:Optional[int]
    company_id:Optional[int]
    login_time:time=None 
    logout_time:time=None
    breaks:list[Breaks]
    salary:Optional[float]
    name:Optional[str]
    duty_time:Optional[time]



@router.post('/fakeattendance',tags=['Faker'])
async def fakeAttendance(db: Session = Depends(get_db)):
    return FakeAttendance.addAttendance(db)

@router.post('/fakeemployee',tags=['Faker'])
async def fakeEmployee(db: Session = Depends(get_db)):
    return FakeAttendance.addEmployee(db)

@router.post('/apply-leave')
async def applyleave(current_user:AttendanceUser=Depends(get_current_user_from_bearer),db: Session = Depends(get_db)):
    return None
@router.post('/login',tags=['Employee Login/Verify'])
async def login(phone:int, db: Session = Depends(get_db)):
    employee=AttendanceRepo.get_employee(phone,db)
    if   employee is None:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Employee does not exist.")
    else:
        user=AttendanceRepo.get_user(phone,db)
        if not user:
            AttendanceRepo.create_user(phone,db)
        otp=AttendanceRepo.create_otp(phone,db)
        return {"otp":otp.code}
 

@router.post('/verify-otp',tags=['Employee Login/Verify'])
async def verifyOtp(phone=Body(...),otp:str=Body(...),db: Session = Depends(get_db)):
    
   return AttendanceRepo.verify_otp(otp,phone,db)

class CompanyOut(BaseModel):
    id:int
    company_name:Optional[str]=None
    company_id:Optional[str]=None
    login_time:Optional[time]
    logout_time:Optional[time]
    status:Optional[Status]
    duty_time:Optional[time]
    class Config:
        orm_mode=True

@router.get('/companies',response_model=list[CompanyOut]  ,tags=['Employee Invitations'])#response_model=list[Invitations],
async def get_companies(current_user:AttendanceUser=Depends(get_current_user_from_bearer),db: Session = Depends(get_db)):
    
    if current_user.is_employer:
        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Not Authorized.")
    # employee=AttendanceRepo.employee_companies( (current_user.phone) ,db)
    # allInvitations=AttendanceRepo.getInvitationByCompany(employee.id,db)
    return db.query(EmployeeModel).filter(EmployeeModel.phone==current_user.phone,).all()#EmployeeModel.status!=Status.INIT

class InvitationsResponse(BaseModel):
    invitations:list[Invitations]
    class Config:
        orm_mode=True
@router.get('/invitations',response_model=list[Invitations],tags=['Employee Invitations'])
async def get_invitations(current_user:AttendanceUser=Depends(get_current_user_from_bearer),db: Session = Depends(get_db)):
    employee=AttendanceRepo.get_employee(phone=current_user.phone,db=db)
    allInvitations=AttendanceRepo.getInvitationByCompany(employee.id,db)
    return  allInvitations

    # class Config:
    #     orm_mode=True
        # eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI5ODAwMDAwMDAwIiwiZXhwIjoxNjg4NDU4Njg0fQ.f4-TCAwXEZaTNFhnQkBSeBDTARDL8NKEijSGErFGBrI
@router.get('/get-today-details',response_model=CreateAttendance,tags=['Employee Details'])#,response_model=AttendanceTodayDetailModel)
def get_today_details(companyId:int,current_user:AttendanceUser=Depends(get_current_user_from_bearer),db: Session = Depends(get_db)):
    employee=AttendanceRepo.get_employee(current_user.phone,db,companyId)
 
    today_details=  AttendanceRepo.get_today_details( employee, db, companyId)
    return today_details  
@router.post('/missing-attendance')
async def add_missing_attendance(employeeId:int,attendance:MissingAttendance, db: Session = Depends(get_db),current_user:AttendanceUser=Depends(get_current_user_from_bearer),):
    attendance=AttendanceRepo.missingAttendance(employeeId,attendance)
    return None
@router.post('/attendance-store',response_model=CreateAttendance,tags=['Employee Details'])
async def store_attendance(companyId:int, db: Session = Depends(get_db),current_user:AttendanceUser=Depends(get_current_user_from_bearer),):
    employee=AttendanceRepo.get_employee(current_user.phone,db,companyId)
    attendance=AttendanceRepo.store_attendance(compId=companyId,empId=employee.id,db=db,loginTime=datetime.now().time(),logoutTime=None )

    return attendance
@router.post('/attendance-stop',response_model=CreateAttendance,tags=['Employee Details'])
async def store_attendance(attendanceId:int, db: Session = Depends(get_db),current_user:AttendanceUser=Depends(get_current_user_from_bearer),):
    attendance=AttendanceRepo.store_logout(attendanceId=attendanceId,db=db,logoutTime=datetime.now().time() )

    return attendance
@router.post('/break-store',tags=['Employee Details'])
async def break_store( attendanceId:int, current_user:AttendanceUser=Depends(get_current_user_from_bearer),db: Session = Depends(get_db)):
    break_start=AttendanceRepo.store_break_start(attendanceId,db)
    return break_start

@router.post('/break-stop-store',tags=['Employee Details'])
async def break_stop( break_id:int,current_user:AttendanceUser=Depends(get_current_user_from_bearer),db: Session = Depends(get_db)):
    break_stop_detail=AttendanceRepo.store_break_stop(break_id,db)
    return break_stop_detail
@router.get('all-attendances',tags=['Employee Details'])
def get_all_attendance(companyId:int,current_user:AttendanceUser=Depends(get_current_user_from_bearer),db: Session = Depends(get_db)):
    employee=AttendanceRepo.get_employee(current_user.phone,db)
    return AttendanceRepo.get_all_attendance(companyId,employee.id,db)


@router.get('/profile',tags=['Employee Details'])
async def getProfile(current_user:AttendanceUser=Depends(get_current_user_from_bearer),db: Session = Depends(get_db)):
    return current_user




@router.post('/update-profile',tags=['Employee Details'])
async def updateProfile(profile:Profile=Form(...),photo:UploadFile(...)=File(None),current_user:AttendanceUser=Depends(get_current_user_from_bearer),db: Session = Depends(get_db)):
    profiledict=profile.__dict__
    if photo:
        url=None 
        
        try:
            # if len(await file.read()) >= 8388608:
            #     return {"Your file is more than 8MB"}
            contents = photo.file.read()
            print(photo.__dict__)
            ext=photo.filename.split(".")[-1]
            url =firebase_upload(contents,ext,photo.filename)
            print(url)
        except Exception as e:
            print(e)
            return e
        photoUrl=None
        
        if url:
            profiledict['photoUrl']=url

    
    updatedUser=AttendanceRepo.update_user(current_user.id,db,profiledict)
    
    return updatedUser
    
@router.get('/accept-invitations/{id}',tags=['Employee Invitations'])#response_model=Invitations,
async def accept_invitations(id:int,status:Status, current_user:AttendanceUser=Depends(get_current_user_from_bearer),db: Session = Depends(get_db)):
    employee=db.get(EmployeeModel,id)#.get_employee(current_user.phone,db,id)
    employee.is_active=True
    employee.status=status
    db.commit()
    db.refresh(employee)
    
    # invitation= AttendanceRepo.updateInvitation(id,db)

    return employee#invitation
     
 

