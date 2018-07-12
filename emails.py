import smtplib
password = input('enter passowrd')
smtpObj = smtplib.SMTP('smtp.gmail.com',587)
type(smtpObj)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login(' poojaag1606@gmail.com',password)
smtpObj.sendmail(' poojaag1606@gmail.com ', ' poojaag1606@gmail.com ','Subject: So long.\nDear Pooja, so long and thanks for all the pics. Sincerely,Meow')
smtpObj.quit()

