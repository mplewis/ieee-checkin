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
