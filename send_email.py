#!/usr/bin/env python
import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase



class Email:
    def __init__(self, user, email_reciever, subject, body, password):
        #User Credetials
        self.email_user = user
        self.email_send = email_reciever
        self.subject = subject
        self.password = password
        self.body = body

    #MIME part, part of the email
    def address(self):
        msg = MIMEMultipart()
        msg['From']= self.email_user
        msg['To']= self.email_send
        msg['Subject']= self.subject

        #body/attachment
        msg.attach(MIMEText(self.body,'plain'))

        #starts secure connection, login
        # msg.attach(part)
        text = msg.as_string()
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(self.email_user, self.password)

        #send email
        server.sendmail(self.email_user, self.email_send, text)
        server.quit()
