import smtplib
from email import message
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime

def send_mail(file,failed_messages,information):
    failed_percentage = 0
    date_time = datetime.now()
    from_addr = 'praktikrealview@gmail.com'
    to_addr = ['cph-cw109@cphbusiness.dk', 'cph-sd152@cphbusiness.dk']
    subject = 'Statstidede parser'
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = from_addr
    msg['To'] = ", ".join(to_addr)
    msg.add_header('Content-Type', 'text')
    html = f"""
    <!DOCTYPE html>
<html>
<body>

<h3>[Information]</h3>

<p>{file}: {information}</p>
</br>
<h3>[Time]</h3>
<p>{date_time}</p>
</br>
<h3>[File]</h3>
<p>{file}
<h3>[Messages with errors]</h3>
<pre>{failed_messages}</pre>

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