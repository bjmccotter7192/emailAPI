import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import Text

class ConnectionException(Exception):
    """Failed to connect to the SMTP server"""
    pass


def formEmailMessage(data):
    sender = data.get('from')
    recipients = data.get('to')
    cc = data.get('cc')
    bcc = data.get('bcc')
    subject = data.get('subject')
    emailBody = data.get('body')

    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ", ".join(recipients)
    msg['Bcc'] = ", ".join(bcc)
    msg['Cc'] = ", ".join(cc)
    msg.attach(MIMEText(emailBody, "plain"))

    return msg


def sendEmail(smtpServerUrl, smtpServerPort, data):
    try:
        s = smtplib.SMTP(smtpServerUrl, smtpServerPort)
        s.set_debuglevel(1)
    except ConnectionException as connEx:
        return { 'message': connEx.args[0] }, 401

    message = formEmailMessage(data)    
    s.sendmail(data.get('from'), data.get('to'), message.as_string())


if __name__ == "__main__":
    emailData = {
        "to": ["bj.mccotter@veteransunited.com"],
        "from": "bjmac@no-reply.com",
        "cc": [],
        "bcc": [],
        "subject": "Finally got everything in order!",
        "body": """
            Will this format?
            I wonder if the new line characters will show up
            Maybe yes
            Maybe no
            The world may never know.        
        """
    }

    print(sendEmail("smtp.veteransunited.com", 25, emailData))