import smtplib
from email.message import EmailMessage

def send_digest(to_email, subject, body):
    msg = EmailMessage()
    msg.set_content(body)
    msg["Subject"] = subject
    msg["From"] = "you@example.com"
    msg["To"] = to_email

    with smtplib.SMTP("localhost") as s:
        s.send_message(msg)

# Example
send_digest("friend@example.com", "Weekly Summary", "Here is what happened this week...")
