from unittest import TestCase, mock
from settings import filenames
from key_logger.mail import EmailService


class TestEmailService(TestCase):

    def test_send_email(self):
        with mock.patch("smtplib.SMTP.sendmail") as sendmail_mock:
            EmailService().send_email({})
            sendmail_mock.assert_called_once()
