import smtplib
import os
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart

send_mail = 'Please enter your Email'
password = 'Issued Password. (16 Characters)'
recv_mail = 'Please enter your email to send photos'
smtp_server = 'smtp.google.com'
port = 587

server = smtplib.SMTP(smtp_server, port)
server.starttls()
server.login(send_mail, password)

msg = MIMEMultipart()
msg['Subject'] = "Success"
msg['From'] = send_mail
msg['To'] = recv_mail

try:
    with open("Camera.jpg", 'rb') as f:
        attach = MIMEApplication(f.read(), _subtype="jpg")
        attach.add_header('content-disposition', 'attachment; filename="Camera.jpg"')
        msg.attach(attach)
except FileNotFoundError:
    print("Error: file Camera.jpg not found.")
    server.quit()

server.sendmail(send_mail, recv_mail, msg.as_string())
os.remove("Camera.jpg")
server.quit()
