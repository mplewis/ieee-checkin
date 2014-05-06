#!/usr/bin/python
import cgi
import cgitb
cgitb.enable()
import os


UPLOAD_TXT_NAME = "checkin.txt"
UPLOAD_TXT_PATH = os.getcwd() + '/' + UPLOAD_TXT_NAME

HTML_TEMPLATE = """<!DOCTYPE html>
<html>
    <head>
        <title>File Upload</title>
        <meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
        <meta http-equiv="refresh" content="1; url=checkin.html" />
    </head>
    <body>
        <h1>File Delete?</h1>
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

print 'content-type: text/html\n\n'

def delete_log_file():
    os.remove(UPLOAD_TXT_NAME)
    f = open(UPLOAD_TXT_NAME)
    f.close()

delete_log_file()

print HTML_TEMPLATE % {'MESSAGE':'Previous log file successfully deleted!'}