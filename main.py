import os
import smtplib

PYTHON_TEST_GMAIL_KEY = os.environ.get('PYTHON_TEST_GMAIL_KEY')
EMAIL_MASTER = os.environ.get('EMAIL_MASTER')

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(EMAIL_MASTER, PYTHON_TEST_GMAIL_KEY)

    subject = "Grab dinner this weekend?"
    body = "How about dinner at 6pm this Saturday"

    msg = f"Subject: {subject}\n\n{body}"

    smtp.sendmail(EMAIL_MASTER, EMAIL_MASTER, msg)