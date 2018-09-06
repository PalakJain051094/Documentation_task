import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from Mailers.GenerateMail import MailGenerate as mg
class Report_Mailer():
    def send_mail(self, status_list,status_report_header):
        body = mg.generateMailBody(self, status_list,status_report_header)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login("test.account @ infobeans.com", "Inf @ 1238$201")
        msg = "\n!!!-----Daily Status Report----!!!"
        server.sendmail("palak.jain@infobeans.com", "mangesh.khude@infobeans.com", msg)

        fromaddr = "test.account @ infobeans.com"
        toaddr = "palak.jain@infobeans.com"
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = "Python email"

        msg.attach(MIMEText(body, 'html'))
        text = msg.as_string()
        server.sendmail(fromaddr, toaddr, text)

