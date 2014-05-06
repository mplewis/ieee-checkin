#!/usr/bin/python
import cgi
import cgitb
cgitb.enable()
import os
import subprocess
import smtplib #Import smtplib for sending function
from email.mime.text import MIMEText #Import the email modules needed

UPLOAD_TXT_NAME = 'checkin.txt'

HTML_TEMPLATE = """<!DOCTYPE html>
<html>
    <head>
        <title>File Upload</title>
        <meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
        <meta http-equiv="refresh" content="1; url=checkin.html" />
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
#create a blank file to send if nothing is available
f = file(UPLOAD_TXT_NAME, 'a')
f.close()

print 'content-type: text/html\n\n'

def send_email():
    if 'subject' not in form:
        print HTML_TEMPLATE % {'MESSAGE':'No subject specified'}
        return

    if 'recipient' not in form:
        print HTML_TEMPLATE % {'MESSAGE':'No recipient specified'}
        return

    subject = form.getfirst('subject').strip()
    recipient = form.getfirst('recipient').strip()
    
    subprocess.call("cat checkin.txt | mail -s " + subject + " " + recipient, shell=True)

def delete_log_file():
    os.remove(UPLOAD_TXT_NAME)

send_email()
#delete_log_file()
print HTML_TEMPLATE % {'MESSAGE':'Email Sent!'}
