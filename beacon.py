#!/usr/bin/env python3
import smtplib
from datetime import datetime
from email.message import EmailMessage
from netifaces import interfaces, ifaddresses, AF_INET
from socket import gethostname

from creds import str_username, str_password, list_recipients

def main():
    # Subject
    now = datetime.now().date()
    str_subject = '['+str(now)+'] '+'IP Update'

    # Message
    str_content = ""
    str_content += str('Host: '+gethostname()+'\n')
    str_content += "#"*10+'\n'
    for ifaceName in interfaces():
        # Build list matching interface name to ip addresses
        addresses = [i['addr'] for i in ifaddresses(ifaceName).setdefault(AF_INET, [{'addr':'No IP addr'}] )]
        str_content += str(ifaceName+' - '+', '.join(addresses)+'\n')
    print(str_content)

    # Sending Email
    sendEmail(list_recipients,str_subject,str_content)

def sendEmail(list_recipients,str_subject,str_content):
    msg = EmailMessage()
    msg['Subject'] = str_subject
    msg.set_content(str_content)

    # Logistics
    try:
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.ehlo()
        server.starttls()
    except:
        print("Issue connecting to Gmail SMTP")
    server.login(str_username,str_password)
    server.sendmail(str_username, list_recipients, str(msg))
    server.quit()
    
if __name__ == "__main__":
    main()
