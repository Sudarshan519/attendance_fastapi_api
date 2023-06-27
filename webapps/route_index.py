
from fastapi.templating import Jinja2Templates
from fastapi import APIRouter
templates=Jinja2Templates(directory='templates')
# router =APIRouter(include_in_schema=False)
from fastapi import Request,Depends,responses,status
from sqlalchemy.orm import Session
from db.session import get_db
templates=Jinja2Templates(directory='templates')
router =APIRouter(include_in_schema=False)
@router.get("/")
# @auth_required
async def home(request: Request, db: Session = Depends(get_db),msg:str = None):   #new
    # jobs = list_jobs(db=db)
    cookie_exist=True if request.cookies.get('name') is not None else False
    return templates.TemplateResponse(
        "base.html", {"request": request},# "jobs": jobs,"msg":msg,"name": "Welcome "+request.cookies.get('name')} if cookie_exist else {"request": request, "jobs": jobs,"msg":msg,}  #new
    )
