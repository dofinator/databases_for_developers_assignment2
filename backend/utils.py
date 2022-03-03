import smtplib
from email import message
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
import csv

def send_mail(name, medicine, email):
    from_addr = 'praktikrealview@gmail.com'
    to_addr = email
    subject = 'Renewal of medicine'
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = from_addr
    msg['To'] = email
    msg.add_header('Content-Type', 'text')
    html = f"""
    <!DOCTYPE html>
<html>
<body>

<p>Dear {name}</p>
<p>It is time for your renewal of {medicine}. You are able to pick up your prescription at any pharmacy you wish.</p>
<p>Kind regards</p>
<p>Apoteket</p>
</br>
</body>
</html>

    """
    part2 = MIMEText(html, "html")
    msg.attach(part2)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_addr, 'Realview152109')
    server.sendmail(from_addr,to_addr,msg.as_string())
    server.quit()

"""
methods selects and return data from the property bag, based on given parameters
where message_name specifies ex. 'proklama', 'dekret' or 'skiftesamling'
and filed_group is the groups og wich a proklama contains, ex. 'afdøde', afødedes aegtefaelle
"""

def write_prescription_info_to_csv(patient_name, medicine, pharmacy, pharmacist):
    with open('backend\prescription_logging.txt', 'a') as file:
        file.write("""Patient who picked up the prescription: {}\nfor the the following medicine: {}\nat this pharmacy: {}\nand handled by the following pharmacist: {} \n\n""".format(patient_name, medicine, pharmacy, pharmacist))
        file.close()

