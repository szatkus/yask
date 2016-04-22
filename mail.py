from email.mime.text import MIMEText
from flask import render_template
from smtplib import SMTP

import config

def send_mail(template_name, subject, recipent, **context):
    body = render_template(template_name, **context)
    message = MIMEText(body, 'html')
    message['Subject'] = subject
    message['To'] = recipent
    message['From'] = config.EMAIL_ADDRESS
    smtp_connection = SMTP(config.SMTP_HOST, config.SMTP_PORT)
    smtp_connection.sendmail(config.EMAIL_ADDRESS, recipent, message.as_string())
    smtp_connection.quit()
