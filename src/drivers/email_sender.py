import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(to_addrs, body):
    from_addr = "vju7rvnfjcpqfatm@ethereal.email"
    login = "vju7rvnfjcpqfatm@ethereal.email"
    password = "sjammEAvJDyMWsvMU5"

    msg = MIMEMultipart()
    msg["From"] = "thiagocosta@email.com"
    msg["To"] = ", ".join(to_addrs)

    msg["Subject"] = "Trip confirmation"
    msg.attach(MIMEText(body, "plain"))

    server = smtplib.SMTP("smtp.ethereal.email", 587)
    server.starttls()
    server.login(login, password)
    text = msg.as_string()

    for email in to_addrs:
        server.sendmail(from_addr, email, text)

    server.quit()
