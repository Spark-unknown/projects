import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(subject, message, from_addr, to_addr, password):
    msg = MIMEMultipart()
    msg['From'] = "priyanshurathod518@gmail.com"
    msg['To'] = "amiscirntific"
    msg['Subject'] = "this is a sample main"

    body = message
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_addr, password)
    text = msg.as_string()
    server.sendmail(from_addr, to_addr, text)
    server.quit()

subject = "Test Email"
message = "This is a test email sent using Python."
from_addr = "priyanshurathod518@gmail.com"
to_addr = "priyanshurathod518@gmail.com"
password = "amiscientific"

send_email(subject, message, from_addr, to_addr, password)