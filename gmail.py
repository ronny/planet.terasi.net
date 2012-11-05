import smtplib
import os

class Gmail:
    def __init__(self):
        self.sender_email = os.environ.get('GMAIL_SMTP_USER', 'nobody@gmail.com')
        self.sender_password = os.environ.get('GMAIL_SMTP_PASSWORD', "I'm not stupid, mate.")

    def send(self, **kwargs):
        smtp = smtplib.SMTP("smtp.gmail.com", 587)
        smtp.ehlo()
        smtp.starttls()
        smtp.login(self.sender_email, self.sender_password)

        recipient = kwargs.get("recipient", os.environ.get('DEFAULT_EMAIL_RECIPIENT', 'nobody@gmail.com'))
        headers = [
            'To: ' + recipient,
            'From: ' + self.sender_email,
            'Subject: ' + kwargs.get("subject", "Planet Terasi Feedback"),
        ]
        body = kwargs.get("body", "(empty)")
        message = "\n".join(headers) + "\n\n" + body
        smtp.sendmail(self.sender_email, recipient, message)
        smtp.close()
