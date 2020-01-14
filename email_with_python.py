import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Rahul Kalwar'
email['to'] = 'kalwar.rahul@gmail.com'
email['subject'] = 'Hey There!!!'

email.set_content("Ohh!, its worked.")

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("emailwithpython8@gmail.com", 'Welcome@123')
    smtp.send_message(email)