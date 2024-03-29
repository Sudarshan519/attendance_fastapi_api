import smtplib
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders
import os
from typing import List

from fastapi import BackgroundTasks
from core.config import settings
# from dotenv import load_dotenv

# load_dotenv()

def sendEmail(smtpHost, smtpPort, mailUname, mailPwd, fromEmail, mailSubject, mailContentHtml, recepientsMailList, attachmentFpaths):
   # create message object
   print(mailContentHtml)
   msg = MIMEMultipart()
   msg['From'] = fromEmail
   msg['To'] = ','.join(recepientsMailList)
   msg['Subject'] = mailSubject
   # msg.attach(MIMEText(mailContentText, 'plain'))
   msg.attach(MIMEText(mailContentHtml, 'html'))


   # create file attachments
   for aPath in attachmentFpaths:
       # check if file exists
       part = MIMEBase('application', "octet-stream")
       part.set_payload(open(aPath, "rb").read())
       encoders.encode_base64(part)
       part.add_header('Content-Disposition',
                       'attachment; filename="{0}"'.format(os.path.basename(aPath)))
       msg.attach(part)


   # Send message object as email using smptplib
   s = smtplib.SMTP(smtpHost, smtpPort)
   s.starttls()
   s.login(mailUname, mailPwd)
   msgText = msg.as_string()
   sendErrs = s.sendmail(fromEmail, recepientsMailList, msgText)
   print(sendErrs)
   s.quit()


   # check if errors occured and handle them accordingly
#    if not len(sendErrs.keys()) == 0:
#        raise Exception("Errors occurred while sending email", sendErrs)




# mail server parameters
smtpHost = "smtp.gmail.com"
smtpPort = 587
mailUname =settings.MAIL_UNAME# os.environ.get("MAIL_UNAME")
mailPwd =settings.MAIL_PASS# os.environ.get("MAIL_PASS")
fromEmail =settings.MAIL_UNAME# 'sudarshanshrestha519@gmail.com'


# mail body, recepients, attachment files
mailSubject = "test subject"
mailContentHtml = "Hi, Hope u are fine. <br/> This is a <b>test</b> mail from python script using an awesome library called <b>smtplib</b>"
# recepientsMailList = ["sudarshanshrestha519@gmail.com"]
attachmentFpaths = []#["smtp.png", "poster.png"]
# sendEmail(smtpHost, smtpPort, mailUname, mailPwd, fromEmail,
#          mailSubject, mailContentHtml, recepientsMailList, attachmentFpaths)
def write_notification(email: List, message:str="",subject:str="",body:str=""):
    sendEmail(smtpHost, smtpPort, mailUname, mailPwd, fromEmail,
            subject, body, email, attachmentFpaths)
    with open("log.txt", mode="a") as email_file:
        content = f"notification for {email}: {message}\n"
        email_file.write(content)

# app=APIRouter()
# @app.post("/send-notification/{email}")
# async def send_notification(email: str, background_tasks: BackgroundTasks):
#     background_tasks.add_task(write_notification, email, message="some notification")
#     return {"message": "Tasks are happening in background"}

class EmailService:
    @staticmethod
    def sendMailTo(email:List[str],title:str,body:str,):
        BackgroundTasks.add_task( sendEmail,smtpHost, smtpPort, mailUname, mailPwd, fromEmail,
            title, body, email, attachmentFpaths)
        
    @staticmethod
    def send_mail_from_background( background_tasks: BackgroundTasks,email=[],subject:str=None,body:str=None):
       
        print(email)
        background_tasks.add_task(write_notification,  (email), message="some notification",subject=subject,body=body)