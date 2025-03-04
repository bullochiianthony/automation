

#import libraries
#Set up your email enviornment for export of email delivery.
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.application import MIMEApplication
from email.utils import formatdate, COMMASPACE

def create_email_msg(email_body_1, email_body_2, email_body_3, newline_char='\n'):
  email_msg = f"Good Morning,{newline_char}{newline_char}"\
    "You are amazing!."\
    f"{newline_char}{newline_char}"\
    f"{email_body_1}{newline_char}"\
    f"{email_body_2}{newline_char}"\
    f"{email_body_3}{newline_char}{newline_char}Thank you,{newline_char}Capital One, etc{newline_char}{newline_char}"\
    "Note: This email was generated by an automated script."
  return email_msg

def send_email(send_from, send_to, cc_to, subject, text, files=None,server="ponyex.capitalone.com", text_type='plain'):
    if not isinstance(send_to, list):
        send_to = [send_to]
    if not isinstance(cc_to, list):
        cc_to = [cc_to]
    msg = MIMEMultipart()
    send_from = send_from
    msg['From'] = send_from
    msg['To'] = COMMASPACE.join(send_to)
    msg['Cc'] = COMMASPACE.join(cc_to)
    msg['Subject'] = subject
    msg.attach(MIMEText(text, text_type))
    for tf in files or []:
        with open(tf, "rb") as temp_file:
            part = MIMEApplication(
                temp_file.read(),
                Name=os.path.basename(tf)
            )
        part['Content-Disposition'] = f'attachment; filename="{os.path.basename(tf)}"'
        msg.attach(part)
    smtp = smtplib.SMTP(server)
    send_to = send_to + cc_to
    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.close()

#Command ------
#Send email to recipient
#email_from = Enter email in which you would like to send your email from.
#send_to = Enter in email (list of emails can be inputted here as well) to send to.
#cc_to = Enter in an email you would like to "CC".  It's best practice to CC the email you are sending from for record keeping purposes.
#subject_line = Enter in a subject header to title of your choice you would like to appear in the email list.
#create_email_msg = Enter an additional message of your choice or you can share a weblink of your choosing.

send_email('email_from', 'send_to', 'cc_to', 'subject_line', create_email_msg('link', 'link2', 'link3'))
