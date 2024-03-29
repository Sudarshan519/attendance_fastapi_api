 
from datetime import date, datetime, time, timedelta
from fastapi import APIRouter, Body, Depends, File, Form, HTTPException, UploadFile,status
from psycopg2 import IntegrityError
from pydantic import BaseModel, Field
from sqlalchemy import func, select
from apps.attendance_system.route_login import get_current_user_from_token,get_current_user_from_bearer
from core.config import settings
from db.models.attendance import  AttendanceModel, AttendanceUser, EmployeeModel, Notifications,Otp,CompanyModel
from requests import Session
from db.session import get_db
from fastapi import Depends, HTTPException, Request
from core.security import create_access_token
from typing import Optional
from db.repository.attendance_repo import AttendanceRepo
from schemas.attendance import BusinessLeaveDayType, Company, CompanyBase, CompanyCreate, NotificationBase, Status
from other_apps.week_util import getMonthRange, getWeekDate
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from sqlmodel.ext.asyncio.session import AsyncSession
# 9863450107
# 0689
# {
#   "phone": "9863450107",
#   "otp": "0726"
# }eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI5ODYzNDUwMTA3IiwiZXhwIjoxNjg4NjYxMzk3fQ.DGBN1ULWnN9db1_QMFLrQ4c8UmpZFqeEljuOtaIeatU
router =APIRouter(prefix='/api/v1', include_in_schema=True, tags=[])
import random
import json

@router.get('/import-db',tags=['Import/Export'])
async def import_db(db: Session = Depends(get_db)):
 
    with open("exported_data.json", "r") as f:
        result=json.load(f)
        # print(result)
    if result is None:
        return {}
    else:
        data=AttendanceRepo.import_db_from_json(result,db)
    #     print(result)
    print(data)    
    
    return data



@router.get('/export-db',tags=['Import/Export'])
async def export_db(db: Session = Depends(get_db)):
    data=AttendanceRepo.export_db(db)
    with open("exported_data.json", "w") as f:
        result=json.dump( (jsonable_encoder(data)),f)
    #     print(result)
    print(data)    
    
    return data

@router.post('/add-notification',tags=['Employer Add Notification'])
async def create_notification(notifiation:NotificationBase=None,db: Session = Depends(get_db),):
    # employee=db.get(EmployeeModel,notifiation.user_id)
    user=db.get(AttendanceUser,notifiation.user_id)
    # notifiation.user_id=user.id
    # user.fcm_token
    return AttendanceRepo.addNotifications(notifiation,db,)

@router.get('/notifications')
async def notifications(db:Session=Depends(get_db)):
    return AttendanceRepo.notification(db,)#companyId

@router.get('/overall-daily-report',tags=['Overall'])
async def overallDailyReport(companyId:int,db:Session=Depends(get_db)):
    dates= getWeekDate( )
    attendee_weekly= db.query(AttendanceModel).where(AttendanceModel.company_id==companyId,AttendanceModel.attendance_date.between(dates[0],dates[1])).count()
    all=db.query(AttendanceModel).count()   
    print(all)  
    print(attendee_weekly)
    datetoday=datetime.now()
    dates= getMonthRange( datetoday.year,datetoday.month)
    attendee_monthly=db.query(AttendanceModel).where(AttendanceModel.company_id==companyId,AttendanceModel.attendance_date.between(dates[0],dates[1])).count()
    print(attendee_monthly)
    return db.query(AttendanceModel).all()
    pass

@router.get('/overall-weekly-report',tags=['Overall'])
async def overallDailyReport(companyId:int,db:Session=Depends(get_db)):
    pass
@router.get('/overall-monthly-report',tags=['Overall'])
async def overallDailyReport(companyId:int,db:Session=Depends(get_db)):
    pass

@router.get('/overall-annual-report',tags=['Overall'])
async def overallDailyReport(companyId:int,db:Session=Depends(get_db)):
    pass
@router.get('/companies',tags=['Companies'],response_model=list[CompanyCreate])
async def get_companies(db: Session = Depends(get_db),current_user:AttendanceUser=Depends(get_current_user_from_bearer)): 
    now=datetime.now()
    print(now)
    companies_list=AttendanceRepo.companies_list(current_user,db) 
    
    # data={'companines':list(filter(lambda x:x.is_active==True  ,companies_list)),'inactive':list(filter(lambda x:x.is_active==False ,companies_list))}
    # print( datetime.now())
    return companies_list
@router.get('/company',tags=['Companies'],response_model=CompanyCreate)
async def get_company_by_id(companyId:int,db: Session = Depends(get_db),current_user:AttendanceUser=Depends(get_current_user_from_bearer)): 
    return db.get(CompanyModel,companyId)
class BaseAttendanceUser(BaseModel):
    phone:str
    otp:str
    
class UpdateUser(BaseModel):
    name:str
    email:str
    dob:date
    class Config:
        orm_mode=True
        
class UpdatePhone(BaseModel):
    current_phone:int
    new_phone:int
    class Config:
        orm_mode=True
class AttendanceReport(BaseModel):
    name:str
    attendance_date:date
    login_time=time
    logout_time=time


# class Company(BaseModel):
#     name:str
#     address:Optional[str]
#     start_time:Optional[time]
#     end_time:Optional[time]
#     established_date:Optional[date] 
#     class Config():  #to convert non dict obj to json
#         schema_extra = {
#             "example": { 
#                     "name": "string",
#                     "address": "string",
#                     "start_time": "10:10",
#                     "end_time": "10:30",
#                     "established_date": "2023-06-30"
#             }
#         }
#         orm_mode = True
#         allow_population_by_field_name = True
#         arbitrary_types_allowed = True
        
        
class Employee(BaseModel):
    name:str
    login_time:time
    logout_time:time
    phone:int
    salary:float
    duty_time:time

    class Config():  #to convert non dict obj to json
        schema_extra={
            "example":{
            "name": "string",
            "login_time": "10:10",
            "logout_time": "10:10",
            "phone": 9800000000,
            "salary": 0,
            "duty_time": "10:50"
            }
        }
        orm_mode = True

@router.get('/profile',tags=['Employer Details'])
async def getProfile(current_user:AttendanceUser=Depends(get_current_user_from_bearer),db: Session = Depends(get_db)):
    return current_user


@router.get('/all-leave')#,response_model=AllLeave)
async def allleave(company_id:int,db: Session = Depends(get_db)):

    return AttendanceRepo.get_all_leaves(compId= company_id,empId=None, db=db)
    

@router.get('/monthly-report',tags=[ 'Employer Report'])
async def getMonthlyReport(companyId:int=None ,employeeId:int=None, db:Session= Depends(get_db),page:int=1,limit=100):
    return AttendanceRepo.employeeWithAttendanceMonthlyReport(db,companyId,employeeId,page,limit)


@router.get("/weekly-report",tags=[ 'Employer Report'])
async def weeklyreport( employeeId:int=None, db: Session = Depends(get_db)):
    dates= getWeekDate()
    weekdata=AttendanceRepo.employeewithAttendanceWeeklyReport(db,employeeId)
    # weekdata=AttendanceRepo.getWeeklyAttendance(companyId,dates[0].date(),dates[1].date(), db)
 
    return weekdata
@router.get("/today-report",tags=[ 'Employer Report'])
async def attendance(companyId:int, db: Session = Depends(get_db),page:int=1,limit:int=10):
        return AttendanceRepo.employeeWithDailyReport(companyId,db,page-1,limit)
        # return AttendanceRepo.reportToday(companyId,db)

        # allAttendances=AttendanceRepo.todayReport(companyId,db)
        # return allAttendances
 


@router.get('/users',tags=['Companies'])#,response_model=list[AttendanceUser])
async def all_employers(db: Session = Depends(get_db)):
    return db.query(AttendanceUser).all()


def create_token(user,db):
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": str(user.phone)}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "Bearer"}

def create_otp(phone,db):
    otp=Otp(phone=phone)
    otp.setrand()
    db.add(otp)
    db.commit()
    db.refresh(otp)
    return otp


def create_user(phone,db,is_employer:bool=False):
    try:
        user=AttendanceUser(phone=phone,is_employer=is_employer)
        db.add(user)
        db.commit() 
        db.refresh(user)
        return user
    except Exception as e:
        raise HTTPException(status_code=409, detail="This candidate alredy registered")
        raise HTTPException(status_code=400,detail=f'{e}')
    

def get_user(phone,db):
    user=db.query(AttendanceUser).filter(AttendanceUser.phone==phone).first()
    if not user:
        # return HTTPException(status_code=404,detail="User does not exist.")
        return None
    return user

def update_user(id:int,db,):
    try:
        
        pass
    except:
        pass
def create_company(user:AttendanceUser,db:Session,company:CompanyBase):
    try:
        # name=company.name,address=company.address,start_time=company.start_time,end_time=company.end_time,established_date=company.established_date
        new_company=CompanyModel(**company.dict(), user_id=user.id,is_active=True)
        db.add(new_company)
        db.commit()
        db.refresh(new_company)
 
        return new_company
    except Exception as e:
        return HTTPException(status_code=status.HTTP_409_CONFLICT,detail="Company Name Already Registered.")

def update_company(id,user:AttendanceUser,db:Session,company:Company):
    try:
        new_company=db.get(CompanyModel,id)
        # name=company.name,address=company.address,start_time=company.start_time,end_time=company.end_time,established_date=company.established_date
        # new_company=CompanyModel(**company.dict(), user_id=user.id,is_active=True)
        for key,value in company.dict().items():
            setattr(new_company,key,value)
        # db.add(new_company)
        db.commit()
        db.refresh(new_company)
 
        return new_company
    except Exception as e:
        return HTTPException(status_code=status.HTTP_409_CONFLICT,detail="Company Name Already Registered.")

def companies_list(user:AttendanceUser,db:Session):

    try: 
        companies= db.query(CompanyModel).filter(CompanyModel.user_id==user.id).all()  
        return companies
    except Exception as e:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=e)

def create_employee(user:AttendanceUser,db:Session,employee:Employee,companyId:int):
    try:
        print(employee.dict())
        new_employee=EmployeeModel(**employee.dict(), user_id=user.id,company_id=companyId)
        db.add(new_employee)
        db.commit()
        db.refresh(new_employee) 
        print(new_employee)
        return new_employee

    except Exception as e:
        
        print(e)
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=f"Employee is already registered.{e}")

def update_employee_by_id(user:AttendanceUser,employee:Employee,employeeId:int, db):
    employee_update=db.get(EmployeeModel,employeeId)
    # Update the employee record with the new values from the dictionary
    for key, value in employee.dict().items():
        print(key)
        setattr(employee_update, key, value)
    # print(employee)
    db.commit()
    db.refresh(employee_update) 
    return employee_update 
@router.get('/get-employee-by-id',tags=['Companies'])
async def getEmployeeById(id:int,db: Session = Depends(get_db)):
    return db.get(EmployeeModel,id)
# def get_employee_by_id(user:AttendanceUser, employeeId:int,companyId:int,db):
@router.post("/register",tags=['Employer Register/Login'])#response_model = BaseAttendanceUser)
async def signup(phone:int,db: Session = Depends(get_db)):
    try:
        eixst_user=get_user(phone,db)
        if eixst_user==None:
            user=create_user(phone,db,is_employer=True ) 
        else:
            pass
        otp=create_otp(phone,db)
    except Exception as e:
        raise HTTPException(status_code=409, detail=f"This email alredy registered{e}")

 
    return BaseAttendanceUser(phone=phone,otp=otp.code)

@router.post('/resend-otp',tags=['Employer Register/Login'])
async def resend_otp(phone:int,db: Session = Depends(get_db)):
    otp=create_otp(phone,db)
    return BaseAttendanceUser(phone=phone,otp=otp.code)

@router.post('/verify-otp',tags=['Employer Register/Login'])
def verify(otp:str=Body(default='0689'),phone:str=Body(default="9863450107"),db: Session = Depends(get_db),):
    return AttendanceRepo.verify_otp(otp,phone,db)
    otp=db.query(Otp).filter(Otp.phone==phone).order_by(Otp.id.desc()).first()

    if otp is not None:
        user=db.query(AttendanceUser).filter(AttendanceUser.phone==phone).first()
        
        if otp.code==code:# and otp.isvalid():
            access_token=create_token(user,db)
            if user.is_verified:
                return access_token
            else:    
                user.is_verified=True
                db.commit()
            return access_token
        else:
            return HTTPException(status_code=401,detail=f"Otp does not match.")
    else:
        return HTTPException(status_code=404,detail=f"Otp not found for user {phone}")

 
@router.post('/add-company',tags=['Companies'],response_model=CompanyCreate)#response_model=Company
def add_company(company:Company,businessleaveDays:list[str]=[],governmentleaveDates:list[date]=[],officialholiday:list[date]=[],db: Session = Depends(get_db),current_user:AttendanceUser=Depends(get_current_user_from_bearer)): 
    company=create_company(current_user,db,company)
    # business_leave_day=
    return company
@router.post('/update-company',tags=['Companies'])#response_model=Company
def update_company(id:int,company:Company,db: Session = Depends(get_db),businessleaveDays:list[BusinessLeaveDayType]=[],governmentleaveDates:list[date]=[],officialholiday:list[date]=[],current_user:AttendanceUser=Depends(get_current_user_from_bearer)): 
    company=AttendanceRepo.update_company(id,current_user,db,company)
    for businessleaveDay in businessleaveDays:
        print(businessleaveDay)
    for governmentLeaveDay in governmentleaveDates:
        print(governmentLeaveDay)
    for officeHolidays in officialholiday:
        print(officeHolidays)
    return company



@router.post('/get-companies',tags=['Companies'],response_model=list[CompanyCreate])
def all_companies(current_user:AttendanceUser=Depends(get_current_user_from_bearer),db: Session = Depends(get_db)):
    # print(current_user)
    company_list=AttendanceRepo.companies_list(user=current_user,db=db)
    
    return {"active":company_list}
posts=[]


@router.post('/add-employee',tags=['Companies'])
def add_employee(employee:Employee,companyId:int, current_user:AttendanceUser=Depends(get_current_user_from_bearer),db: Session = Depends(get_db)):
    print(employee)
    employee=create_employee(current_user,db,employee,companyId)
    return employee  
@router.get('/employee-by-id')
async def getEmployee(employeeId:int, current_user:AttendanceUser=Depends(get_current_user_from_bearer),db: Session = Depends(get_db)):
    try:
        return db.get(EmployeeModel,id)
    except Exception as e:
        return HTTPException(status_code=404,detail='Employee not found')
@router.post('/update-employee',tags=['Companies'])
def update_employee(id:int,employee:Employee,companyId:int, current_user:AttendanceUser=Depends(get_current_user_from_bearer),db: Session = Depends(get_db)):
    employee=update_employee_by_id(current_user,employee,id,companyId,db)
    return employee  
@router.post('/add-approver',tags=['Companies'])
def add_approver(id:int, db: Session = Depends(get_db)):#current_user:AttendanceUser=Depends(get_current_user_from_bearer),
    approver=AttendanceRepo.add_approver(id,db)
    return approver

@router.get("/approvers")
async def allApprovers(companyId:int, db: Session = Depends(get_db)):#current_user:AttendanceUser=Depends(get_current_user_from_bearer),
    approver=AttendanceRepo.allApprovers(companyId,db)
    return approver

@router.post("/send-invitation",tags=[ 'Companies'])
def sendInvitation(employeeId,current_user:AttendanceUser=Depends(get_current_user_from_bearer),db: Session = Depends(get_db)):
    employee=db.get(EmployeeModel,employeeId)
    employee.status=Status.INVITED
    db.commit()
    db.refresh(employee)
    return employee
    # invitation=AttendanceRepo.create_company_invitation(employeeId,companyId,db)
    # return invitation
def allemployees(id,db):
    return db.query(EmployeeModel).filter(EmployeeModel.company_id==id).all()
@router.get('/employee',tags=[ 'Companies'])
def all_employee(companyId:int,db: Session = Depends(get_db)):# current_user:AttendanceUser=Depends(get_current_user_from_bearer),
    employeelist=allemployees(companyId,db)
    return employeelist
# @router.post("/posts",  tags=["posts"])#dependencies=[Depends(JWTBearer())],
# def add_post(post,current_user:AttendanceUser=Depends(get_current_user_from_bearer)):
#     print(current_user)
#     # post.id = len(posts) + 1
#     # posts.append(post.dict())
#     return {
#         "data": "post added."
#     }


import inspect
from typing import Type

from fastapi import Form
from pydantic import BaseModel
from pydantic.fields import ModelField

def as_form(cls: Type[BaseModel]):
    new_parameters = []

    for field_name, model_field in cls.__fields__.items():
        model_field: ModelField  # type: ignore

        new_parameters.append(
             inspect.Parameter(
                 model_field.alias,
                 inspect.Parameter.POSITIONAL_ONLY,
                 default=Form(...) if model_field.required else Form(model_field.default),
                 annotation=model_field.outer_type_,
             )
         )

    async def as_form_func(**data):
        return cls(**data)

    sig = inspect.signature(as_form_func)
    sig = sig.replace(parameters=new_parameters)
    as_form_func.__signature__ = sig  # type: ignore
    setattr(cls, 'as_form', as_form_func)
    return cls

@as_form
class FileUploadModel(BaseModel):
    name:list[str]
    # password:str=Field(None)
 
    # label:str=Field(...)
    uploadfile:list[UploadFile]

@router.post('/upload-files')
def upload(uploadfile:list[FileUploadModel]=Depends(FileUploadModel.as_form) ):
    return {}