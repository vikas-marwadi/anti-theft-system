import smtplib
import imghdr
from email.message import EmailMessage


def email_alert(subject, body, to, file): 
    msg = EmailMessage()
    msg.set_content(body)
    
    user = 'server eamil adrress'
    password = 'password'
    
    msg['subject'] = subject
    msg['to'] = to
    msg['from'] = user
    with open(file, 'rb') as fp:
            img_data = fp.read()
    msg.add_attachment(img_data, maintype='image', subtype=imghdr.what(None, img_data), filename='Intuder photos')
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)
    
    server.quit()

if __name__ == '__main__':
    email_alert('From: Anti-Theft Alert System', "Hey, In your shop Intruder Detected", 'email address', 'Capture.jpg')
