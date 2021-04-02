import getpass
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from settings import email_address, to_address, password


class EmailService:

    @staticmethod
    def send_email(filename, attachment):
        msg = MIMEMultipart()
        msg['From'] = email_address
        msg['To'] = to_address
        msg['Subject'] = "Log File"
        body = "Body_of_the_mail"
        msg.attach(MIMEText(body, 'plain'))
        filename = filename
        attachment = open(attachment, 'rb')
        p = MIMEBase('application', 'octet-stream')
        p.set_payload((attachment).read())
        encoders.encode_base64(p)
        p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
        msg.attach(p)
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(email_address, password)
        text = msg.as_string()
        s.sendmail(email_address, to_address, text)
        s.quit()
