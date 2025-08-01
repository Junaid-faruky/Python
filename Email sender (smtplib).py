# 15. Email sender (smtplib)
import smtplib
server = smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
# server.login("your_email","your_password")
# server.sendmail("from","to","Hello!")
print("Email setup ready")
