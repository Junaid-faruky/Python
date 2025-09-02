import smtplib

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login("your_email@gmail.com", "your_password")
server.sendmail("your_email@gmail.com", "receiver@gmail.com", "Subject: Hi\n\nThis is an automated mail.")
server.quit()
