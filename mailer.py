import smtplib, ssl
from secret import google_app_password as gap

HOST = "smtp.gmail.com"
PORT = 465


def send_mail(subject, message, receiver=gap.USER):
    context = ssl.create_default_context()

    message = f"Subject: {subject}\n{message}"

    with smtplib.SMTP_SSL(HOST, PORT, context=context) as server:
        server.login(gap.USER, gap.PASSWORD)
        print(f'sending mail "{subject}" to {receiver}...')
        server.sendmail(gap.USER, receiver, message.encode('utf-8'))
        print('email sent')
