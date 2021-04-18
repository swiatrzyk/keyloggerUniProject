import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from settings import email_address, to_address, password, file_path


class EmailService:

    @staticmethod
    def send_email(filenames):
        msg = MIMEMultipart()
        msg['From'] = email_address
        msg['To'] = to_address
        msg['Subject'] = "Log File"
        body = "Body_of_the_mail"
        msg.attach(MIMEText(body, 'plain'))

        for _, filename in filenames.items():
            attachment = open(file_path + "\\" + filename, 'rb')
            p = MIMEBase('application', 'octet-stream')
            p.set_payload(attachment.read())
            encoders.encode_base64(p)
            p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
            msg.attach(p)

        try:
            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.starttls()
            s.login(email_address, password)
            text = msg.as_string()
            s.sendmail(email_address, to_address, text)
            s.quit()
            print("Sending email succeeded")
        except Exception:
            print("Sending email failed")
