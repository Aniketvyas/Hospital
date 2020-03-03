 import smtplib
import os
 
 
 with smtplib.SMTP('smtplib.gmail.com' , 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()
           

            smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
            subject = "E-mail verification"
            body = "hello world"
            msg = f'subject:{subject}\n\n{body}'
            smtp.sendmail(EMAIL_ADDRESS, email , msg) with smtplib.SMTP('smtplib.gmail.com' , 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()
           

            smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
            subject = "E-mail verification"
            body = "hello world"
            msg = f'subject:{subject}\n\n{body}'
            smtp.sendmail(EMAIL_ADDRESS, email , msg)