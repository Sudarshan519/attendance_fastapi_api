 
from datetime import datetime,timedelta
from sqlalchemy import Column,Integer, String,Boolean, ForeignKey,Date,Time,Float,BigInteger,DateTime,UniqueConstraint,Table,Enum
from sqlalchemy.orm import relationship
from db.base import Base
import random
 
from schemas.attendance import Status
from fastapi import Depends
from requests import Session
from db.session import get_db
# Declare Classes / Tables
# employee_companies = Table('employee_companies', Base.metadata,
#     Column('employee_id', ForeignKey('employeemodel.id'), primary_key=True),
#     Column('company_id', ForeignKey('companymodel.id'), primary_key=True)
# )

class Otp(Base):
    id=Column(Integer,primary_key=True,index=True)
    code=Column(String,nullable=False)
    phone=Column(BigInteger,nullable=False)
    created_at=Column(DateTime)  
    
    def setrand(self):
        self.code="{:04d}".format (random.randint(0, 9999))
        self.created_at=datetime.now()
    def isvalid(self):
        now:DateTime=datetime.now()
        return (now-self.created_at)<timedelta(minutes=2)
    

# class AttendanceUser(Base):
#     id = Column(Integer,primary_key=True,index=True)
#     phone=Column(Integer,unique=True)
#     photoUrl=Column(String,default='')
#     name=Column(String,default='')
#     otp = Column(Integer,ForeignKey('otp.id'))
 

class AttendanceUser(Base):
    id = Column(Integer,primary_key=True,index=True)
    phone=Column(BigInteger,unique=True,nullable=True,)
    photoUrl=Column(String,default='')
    name=Column(String,default='')
    email=Column(String,default='')
    is_verified=Column(Boolean,default=False)
    is_employer=Column(Boolean,default=False)
    is_approver=Column(Boolean,default=False)
    otp_id = Column(Integer,ForeignKey('otp.id'),nullable=True)
    employee_id=Column(Integer,ForeignKey('employeemodel.id'),nullable=True)
    # employee=relationship("EmployeeModel")
    dob=Column(Date,nullable=True)
    # def employee(self,db: Session = Depends(get_db), ):
    #     employee=AttendanceRepo.get_employee(self.phone,db)
    #     return employee
    # @property
    # def salary(self):
    #     return self.employee.salary
class CompanyModel(Base):
    id = Column(Integer,primary_key=True,index=True)
    name=Column(String, unique=True)
    address=Column(String)
    start_time=Column(Time)
    end_time=Column(Time)
    established_date=Column(Date) 
    is_active=Column(Boolean,default=True)
    user_id =  Column(Integer,ForeignKey("attendanceuser.id"),nullable=True)
    

class EmployeeModel(Base):
    id = Column(Integer,primary_key=True,index=True)
    phone=Column(BigInteger,unique=True)
    name=Column(String,nullable=False)
    login_time=Column(Time)
    logout_time=Column(Time)
    salary=Column(Float)
    duty_time=Column(Time)
    is_active=Column(Boolean,default=False)
    user_id =  Column(Integer,ForeignKey("attendanceuser.id",),default=1)
    company_id =  Column(Integer,ForeignKey("companymodel.id",),default=1)
    attendance = relationship("AttendanceModel", back_populates="employee")
    # eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI5ODAwMDAwMDAwIiwiZXhwIjoxNjg4NDU2MTM1fQ.PeAR8N5yJ1Nn5wucM6hh9Pzmjc3ATwtScT_LBvc7mkw
    # status=Column(Enum(Status),default=False)
    
    # company = relationship("companymodel",)


class BreakModel(Base):
    id = Column(Integer,primary_key=True,index=True)
    break_start=Column(Time)
    break_end=Column(Time)
    company_id =  Column(Integer,ForeignKey("employeemodel.id",),default=1)
    attendance_id=Column(Integer,ForeignKey('attendancemodel.id'), nullable=True)
    attendance=relationship("AttendanceModel",back_populates='breaks')
def calcTime(enter,exit):
    format="%H:%M:%S"
    #Parsing the time to str and taking only the hour,minute,second 
    #(without miliseconds)
    enterStr = str(enter).split(".")[0]
    exitStr = str(exit).split(".")[0]
    #Creating enter and exit time objects from str in the format (H:M:S)
    enterTime = datetime.strptime(enterStr, format)
    exitTime = datetime.strptime(exitStr, format)
    return exitTime - enterTime
class AttendanceModel(Base):
    id = Column(Integer,primary_key=True,index=True)
    attendance_date=Column(Date )
    login_time=Column(Time,nullable=False)
    logout_time=Column(Time,nullable=True,)
    # breaks= Column(Integer,ForeignKey('breakmodel.id'),default=1)
    company_id =  Column(Integer,ForeignKey("companymodel.id",),default=1)
    employee_id=Column(Integer,ForeignKey("employeemodel.id",),default=1)
    breaks=relationship("BreakModel",back_populates='attendance')
    employee = relationship("EmployeeModel", back_populates="attendance")
    @property
    def hours_worked(self):
        if self.logout_time is not None:
            return calcTime(self.login_time,self.logout_time)/(60*60)
        return 4##calcTime(self.login_time+timedelta(hours=4))
    @property
    def salary(self):
        return self.employee.salary
    
    @property
    def duty_time(self):
        return self.employee.duty_time
    
    @property
    def name(self):
        return self.employee.name
    # def breaks(self ,db: Session = Depends(get_db)):
    #     return db.query(BreakModel).filter(BreakModel.attendance==self.id).all()

class EmployeeCompany(Base):
    id = Column(Integer,primary_key=True,index=True)
    employee_id=Column(Integer,ForeignKey('employeemodel.id'),default=1)
    company_id=Column(Integer,ForeignKey('companymodel.id'),default=1)
    is_invited=Column(Boolean,default=True)
    is_accepted=Column(Boolean,default=False)
    is_active=Column(Boolean,default=True)
    employee=relationship("EmployeeModel")#,back_populates="employeemodel")
    company=relationship("CompanyModel",)#back_populates="company")
    status=Column(Enum(Status),default=1,nullable=True)
    # def company_name(self):
    #     print(self.company)
    #     return self.company.name
    # def company_start_time(self):
    #     return self.company.start_time
    # def company_end_time(self):
    #     return self.company.end_time
    # def established_date(self):
    #     return self.company.established_date