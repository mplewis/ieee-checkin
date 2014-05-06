#!/usr/bin/python
import cgi
import cgitb
cgitb.enable()
import os
import smtplib #Import smtplib for sending function
from email.mime.text import MIMEText #Import the email modules needed

UPLOAD_TXT_NAME = 'checkin.txt'
SENDER = 'vuong033@umn.edu'

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

def send_email():
    if 'emailAddress' not in form:
        print HTML_TEMPLATE % {'MESSAGE':'No email specified'}
        return

    if 'subject' not in form:
        print HTML_TEMPLATE % {'MESSAGE':'No subject specified'}
        return

    emailAddress = form.getfirst('emailAddress').strip()
    subject = form.getfirst('subject').strip()

    with open(UPLOAD_TXT_NAME, 'rb') as f:
        msg = MIMEText(f.read())

    s = smtplib.SMTP('localhost')
    s.sendmail(SENDER, emailAddress, msg.as_string())
    s.quit()

def delete_log_file():
    os.remove(UPLOAD_TXT_NAME)

send_email()
delete_log_file()
