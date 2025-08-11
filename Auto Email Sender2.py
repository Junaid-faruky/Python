import smtplib
from email.mime.text import MIMEText

sender = "your_email@gmail.com"
password = "your_password"
receiver = "friend@example.com"

msg = MIMEText("This is a test email sent using Python!")
msg["Subject"] = "Python Email"
msg["From"] = sender
msg["To"] = receiver

server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login(sender, password)
server.sendmail(sender, receiver, msg.as_string())
server.quit()

print("Email sent successfully!")
