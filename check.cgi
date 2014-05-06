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


def save_description(form_field, upload_dir):
    if 'form_field' not in form:
        return False
    try:
        description = form[form_field].value.upper().strip()

        fout = file(upload_dir, 'a')
        if (form_field == "studentID"):
            fout.write(description)
            fout.write('\n')
        else:
            fout.write(description + ":")
        fout.close()
        return True
    except:
        print HTML_TEMPLATE % {'MESSAGE': "Error: description item not in form"}
        return False


def save_card(form_field, upload_dir):
    if 'form_field' not in form:
        return False

    raw = form[form_field].value

    # parsing the card information
    # specific for your card
    try:
        start = raw.find('%')
        end = raw.find('?')
        data = raw[start:end].split('^')
        name = data[5].split(',')
        first_name = name[1][1:].split(' ')[0]
        last_name = name[0]
        idNum = data[1]

        fout = file(upload_dir, 'a')
        fout.write(first_name + ':')
        fout.write(last_name + ':')
        fout.write(idNum)
        fout.write('\n')
        fout.close()

        print HTML_TEMPLATE % {'MESSAGE': 'Description uploaded successfully in ' + UPLOAD_TXT_PATH}
        return True

    except:
        print HTML_TEMPLATE % {'MESSAGE': "Error: Error reading Ucard"}
        return False

print 'content-type: text/html\n\n'
save_card("cardtxt", UPLOAD_TXT_PATH)
save1 = save_description("firstname", UPLOAD_TXT_PATH)
save2 = save_description("lastname", UPLOAD_TXT_PATH)
save3 = save_description("studentID", UPLOAD_TXT_PATH)

if (save1 and save2 and save3):
    print HTML_TEMPLATE % {'MESSAGE': 'Description uploaded successfully in ' + UPLOAD_TXT_PATH}
