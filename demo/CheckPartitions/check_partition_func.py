from email.mime.text import MIMEText
import smtplib, sys, base64
import subprocess
import socket

smtp_server = "smtp.gmail.com"
fromaddr = "akif05@gmail.com"
toaddr = "akif05@gmail.com"
subject = "Low disk space warning"
passwd_enc = b'RmlrQHIxNTA4'

def report_via_email(message):
    global smtp_server
    global fromaddr
    global toaddr
    global subject
    global passwd_enc

    msg = MIMEText(message)
    msg["Subject"] = subject
    msg["From"] = fromaddr
    msg["To"] = toaddr

    # Using with no need to use server.quit()!!!
    with smtplib.SMTP(smtp_server, 25) as server:
        server.connect(smtp_server)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(fromaddr, base64.b64decode(passwd_enc).decode("utf-8"))
        text = msg.as_string()
        server.sendmail(fromaddr, toaddr, text)

def report_via_stdout(msg):
    print (msg)

def check_once(options, partition_list):
    proc = subprocess.Popen(["df", "-h"], stdout=subprocess.PIPE)
    hostname = socket.gethostname()
    for line in proc.stdout:
        splitline = line.decode().split()

        for partition in partition_list:

            if splitline[8] == partition:
                percent = int(splitline[4][:-1])
                if percent > options.threshold:
                    message = "WARNING: partition %s is %d%% fill on %s" % (partition, percent, hostname)
                    if options.maillbox:
                        try:
                            report_via_email(message)
                        except Exception as e:
                            print(e)
                    else:
                        report_via_stdout(message)




