import os
import smtplib
import imghdr
from email.message import EmailMessage
import imaplib, email


SEND_EMAIL = False
PYTHON_TEST_GMAIL_KEY = os.environ.get('PYTHON_TEST_GMAIL_KEY')
EMAIL_MASTER = os.environ.get('EMAIL_MASTER')

# Functions to clean obtained data
def get_body(msg):
    if msg.is_multipart():
        return get_body(msg.get_payload(0))
    else:
        return msg.get_payload(None, True)

def search(key,value,con):
    result, data  = con.search(None,key,'"{}"'.format(value))
    return data

def get_emails(result_bytes):
    msgs = []
    for num in result_bytes[0].split():
        typ, data = con.fetch(num, '(RFC822)')
        msgs.append(data)
    return msgs

# Connection
imap_url="imap.gmail.com"
con = imaplib.IMAP4_SSL(imap_url)
con.login(EMAIL_MASTER, PYTHON_TEST_GMAIL_KEY)
con.select("INBOX")

# Filtering messages by subject
msgs = get_emails(search('SUBJECT', 'Subject to test the filter', con))
for msgss in msgs:
    print(get_body(email.message_from_bytes(msgss[0][1])))


# This part will be used in future
if SEND_EMAIL:
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