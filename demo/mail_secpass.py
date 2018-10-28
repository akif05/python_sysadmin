from email.mime.text import MIMEText
import smtplib, sys
import base64
# my_secret = base64.b64encode(b'Fik@r1508')


# data = base64.b64decode(passwd_enc)
# passwd_enc = base64.b64encode(b'plain_text_passwd')
passwd_enc = b'RmlrQHIxNTA4'

## This is working example, message send successfuly! Use for a base if needed (python 3.7)
fromaddr = "akif05@gmail.com"
toaddr = "akif05@gmail.com"
subject = "Low disk space warning"

msg = MIMEText("Disk space on your server is running low (less than 10% free")
msg["Subject"] = subject
msg["From"] = fromaddr
msg["To"] = toaddr

server = smtplib.SMTP('smtp.gmail.com', 25)
server.connect("smtp.gmail.com")
server.ehlo()
server.starttls()
server.ehlo()
# server.login(fromaddr, "Fik@r1508")
server.login(fromaddr, base64.b64decode(passwd_enc).decode("utf-8"))
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()


