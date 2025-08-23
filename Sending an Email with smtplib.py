import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Setup (replace with your actual details)
sender_email = "your_email@gmail.com"
receiver_email = "recipient_email@example.com"
password = "your_app_password"  # Use an App Password for Gmail

message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = "Test Email from Python"

body = "This is a test email sent from a Python script!"
message.attach(MIMEText(body, "plain"))

# Uncomment and configure to actually send
# with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
#     server.login(sender_email, password)
#     server.sendmail(sender_email, receiver_email, message.as_string())

print("Email composed (commented out for safety).")
