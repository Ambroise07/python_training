#coding:utf-8
import smtplib, ssl
from email.mime.text import MIMEText
#from email.headerregistry import Address
from email.mime.multipart import MIMEMultipart
port = 465
secure_con = ssl.create_default_context()

mailadresse = ['informatutos7@gmail.com']
for i in mailadresse :

    mail_content = {
        'From':'InformaUrl <noreply@informatutos.com>',
        'To': 'Tests <'+i+'>',
        'Subject':'Confirmation de compte',

        }

    mail_text = " <h6>Bonjour votre compte a été créer </h6>"
    text_content = MIMEText(mail_text, "html")

    message = MIMEMultipart()
    message['From'] = mail_content['From']
    message['To'] = mail_content['To']
    message['Subject'] = mail_content['Subject']
    message.attach(text_content)


    with smtplib.SMTP_SSL(host='smtp.zoho.com', port=port, context = secure_con) as Server :
        try :
            if Server.login('noreply@informatutos.com', 'Rootforuserroot07$') :
                if Server.sendmail('noreply@informatutos.com','informatutos7@gmail.com',message.as_string()):
                    Server.close()
        except :
            print("Error")

        
