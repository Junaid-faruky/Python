import smtplib

server = smtplib.SMTP('smtp.example.com', 587)
server.starttls()
server.login("you@example.com", "password")
server.sendmail("you@example.com", "to@example.com", "Subject: Hello\nThis is an email body.")
server.quit()
