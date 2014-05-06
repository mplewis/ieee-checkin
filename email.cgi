#!/usr/bin/python
import cgi
import cgitb
cgitb.enable()
import os
import smtplib #Import smtplib for sending function
from email.mime.text import MIMEText #Import the email modules needed

UPLOAD_TXT_NAME = 'checkin.txt'
SMTP_PORT = 587
SMTP_SERVER = 'smtp.gmail.com'

HTML_TEMPLATE = """<!DOCTYPE html>
<html>
    <head>
        <title>File Upload</title>
        <meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
        <meta http-equiv="refresh" content="1; url=http://z.umn.edu/ieeecheckin" />
    </head>
    <body>
        <h1>File Upload</h1>
        <h1>%(MESSAGE)s</h1>
        <hr>
        <table>
            <tr>
                <td>
                    <a href="checkin.html">Check-In Again</a>
                </td>
            </tr>
        </table>
    </body>
</html>"""

form = cgi.FieldStorage()

print 'content-type: text/html\n\n'

def send_email():
    if 'subject' not in form:
        print HTML_TEMPLATE % {'MESSAGE':'No subject specified'}
        return

    if 'recipient' not in form:
        print HTML_TEMPLATE % {'MESSAGE':'No  specified'}
        return

    if 'sender' not in form:
        print HTML_TEMPLATE % {'MESSAGE':'No sender specified'}
        return

    if 'password' not in form:
        print HTML_TEMPLATE % {'MESSAGE':'No password specified'}
        return

    subject = form.getfirst('subject').strip()
    recipient = form.getfirst('recipient').strip()
    sender = form.getfirst('sender').strip()
    password = form.getfirst('password').strip()

    with open(UPLOAD_TXT_NAME, 'rb') as f:
        msg = MIMEText(f.read())

    session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)

    session.ehlo()
    session.starttls()
    session.ehlo
    session.login(sender, password)

    session.sendmail(sender, recipient, msg.as_string())
    session.quit()

def delete_log_file():
    os.remove(UPLOAD_TXT_NAME)

send_email()
delete_log_file()
