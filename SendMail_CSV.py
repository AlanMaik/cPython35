# -*- coding: utf-8 -*-
import smtplib
import logging
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import csv
import time
import re

logdir = "c:\logsendmail"
if os.path.exists(logdir) != True:
    os.mkdir(logdir)
logging.basicConfig(
    filename = 'c:\\logsendmail\\log.log',
    level = logging.DEBUG,
    format = '[service] %(levelname)-7.7s %(message)s'
    )

def enviaEmail(to):
    msg = MIMEMultipart('alternative')
    msg['Subject'] = 'Subject'
    msg['From'] = "yourmail"
    msg['To'] = to
    text = ""
    html = """
                ---HTML Code---
           """
    part1 = MIMEText(text.encode('utf-8'), 'plain','utf-8')
    part2 = MIMEText(html.encode('utf-8'), 'html','utf-8')
    msg.attach(part1)
    msg.attach(part2)
    try:
        smtp = smtplib.SMTP('host', 587)
        smtp.starttls()
        smtp.login('User', 'password')
        smtp.ehlo()
        smtp.sendmail(msg['From'],msg['To'],msg.as_string())
    except Exception:
        logging.info("Exception %s ..." % (msg['To']))
    smtp.quit()
def SendMailContact():
    with open('file.csv','r') as file:
        contacts = csv.reader(file)
        for to in contacts:
            to = str(to).replace("['","").replace("']", "").strip()
            if validarEmail(to):
                enviaEmail(to)
            else:
                logging.info("%s ..." % to)

            time.sleep(1)

def validarEmail(email):
    EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")
    if not EMAIL_REGEX.match(email):
        return False
    else:
        return True
    
SendMailContact()
