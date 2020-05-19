import os
import smtplib
import imghdr
from email.message import EmailMessage

PYTHON_TEST_GMAIL_KEY = os.environ.get('PYTHON_TEST_GMAIL_KEY')
EMAIL_MASTER = os.environ.get('EMAIL_MASTER')

msg = EmailMessage()
msg['Subject'] = "Am I a business man?"
msg['From'] = EMAIL_MASTER
msg['To'] = EMAIL_MASTER
msg.set_content('I am good talking about finance but my business skills though...')

with open('businessman.png', 'rb') as f:
    file_data = f.read()
    file_name = f.name
    file_type = imghdr.what(file_name)

msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_MASTER, PYTHON_TEST_GMAIL_KEY)
    smtp.send_message(msg)