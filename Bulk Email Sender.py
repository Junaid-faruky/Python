import smtplib
from email.message import EmailMessage

msg = EmailMessage()
msg.set_content("This is a test email")
msg["Subject"] = "Test Mail"
msg["From"] = "your_email@gmail.com"
msg["To"] = "target@example.com"

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login("your_email@gmail.com", "your_password")
    smtp.send_message(msg)

print("Email sent!")
