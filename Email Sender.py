import smtplib

sender = "your@gmail.com"
receiver = "friend@gmail.com"
password = "your_app_password"

with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()
    server.login(sender, password)
    server.sendmail(sender, receiver, "Subject: Hello\n\nThis is a test email.")
