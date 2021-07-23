import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import json
class ConnectionException(Exception):
    """Failed to connect to the SMTP server"""
    pass

def validateInputs(data):
    print("inside of the validate inputss")
    recipients = data.get('To')
    sender = data.get('From')
    body = data.get('Body')

    response = [True, "Success! You sent valid data."]

    if len(recipients) > 0:
        for i in recipients:
            print("inside of the recipients loop")
            if i == "":
                print(f"Checking what i is: {i}")
                response = [False, "To"]
                
    if sender == "":
        print("Inside of the sender if")
        response = [False, "From"]

    if body == "":
        print("Inside of the body if")
        response = [False, "Body"]

    return response

def formEmailMessage(data):
    sender = data.get('From')
    recipients = data.get('To')
    cc = data.get('Cc')
    bcc = data.get('Bcc')
    subject = data.get('Subject')
    emailBody = data.get('Body')

    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ", ".join(recipients)
    msg['Bcc'] = ", ".join(bcc)
    msg['Cc'] = ", ".join(cc)
    msg.attach(MIMEText(emailBody, "plain"))

    return msg

def sendEmail(smtpServerUrl, smtpServerPort, data):
    dataDict = dict(data)
    validated = validateInputs(dataDict)[0]

    if validated:
        sender = dataDict.get('From')
        recipients = dataDict.get('To')

        try:
            s = smtplib.SMTP(smtpServerUrl, smtpServerPort)
            s.set_debuglevel(1)
        except ConnectionException as connEx:
            return { 'message': connEx.args[0] }, 401

        message = formEmailMessage(dataDict)    
        s.sendmail(sender, recipients, message.as_string())
        return { 'success': f"Successfully sent an email to: {recipients}" }
    else:
        return { 'Failure': f"Your {validated[1]} data has an empty string, please correct and try again."}