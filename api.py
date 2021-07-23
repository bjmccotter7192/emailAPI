from emailModel import EmailModel
from emailLogic import sendMail, sendHTMLEmail
from fastapi import FastAPI, HTTPException
import os

smtpServer = "smtp.veteransunited.com"
smtpPort = 25

app = FastAPI(
    title='EmailAPI',
    description="""
        Do you ever just want an easy way to send someone an email?
        Well you have come to the right place! This email api is a
        simple wrapper around the smtplib package that allows users
        to submit a JSON request and send an email to anyone they 
        want. 

        If there are any issues at all please reach out to chefwindows10@gmail.com, THANKS!
    """,
    version="1.0.0"
)

@app.post(
        "/api/v1/sendMail",
        summary="Send an plain text email",
        tags=["SendMail"]
    )
def sendEmail(data: EmailModel):
    """
        SendMail is a fun tool that uses the smtplib package to connect you 
        to the veteransunited smtp server over the encrypted port. Please be
        sure to fill out all the required fields so there is no issue.

        Thanks and enjoy sending those mails!
    """
    return sendMail(smtpServer, smtpPort, data)

@app.post(
        "/api/v1/sendMailHTML",
        summary="Send an html supported email",
        tags=["SendMail"]
    )
def sendHtmlEmail(data: EmailModel):
    """
        SendMail is a fun tool that uses the smtplib package to connect you 
        to the veteransunited smtp server over the encrypted port. Please be
        sure to fill out all the required fields so there is no issue.

        Thanks and enjoy sending those mails!
    """
    return sendHTMLEmail(smtpServer, smtpPort, data)

@app.get(
        "/api/v1/health",
        summary="Health check will determine if service is alive",
        tags=["Health"]
    )
def health_check():
    """Function will return 200 OK if the service is up and running"""
    return "OK"

@app.get(
        "/api/v1/failure",
        summary="Returning 404 using FastAPI HTTPException",
        tags=["404"]
    )
def fail_check():
    """Function will return 404 with a bad message"""
    raise HTTPException(
            status_code=400, 
            detail="Failed to do the thing so we sent 404",
            headers={"X-Error": "Fail_Check returned a 404 because i said so"}
        )