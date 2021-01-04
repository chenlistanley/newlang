import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender='from@runoob.com'
receivers=['75802270@qq.com']
message=MIMEText('python test email', 'plain', 'utf-8')
message['from']=Header('python', 'utf-8')
message['to']=Header('test', 'utf-8')

try:
    smtpObj=smtplib.SMTP('localhost')
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("send mail success")
except smtplib.SMTPException:
    print("send mail failed")
