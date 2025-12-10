import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

message = MIMEMultipart("alternative")

text_content = "This is test email content."

email = "anu0310v@gmail.com"
password = "bxtp hnjx oryz akns"

my_server = smtplib.SMTP('smtp.gmail.com', 587)
my_server.starttls()
my_server.ehlo()
my_server.login(email, password)
    
message.attach(MIMEText(text_content, 'plain'))

my_server.sendmail(from_addr= email, to_addrs="anu0310v@gmail.com", msg=message.as_string())


my_server.quit()