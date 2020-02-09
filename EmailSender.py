import smtplib
email=raw_input("ENTER YOUR GMAIL ADRESS?==> ")
sendmaili=raw_input("ENTER TARGET GMAIL ADRESS==> ")
passw=raw_input("ENTER YOUR GMAIL PASS==> ")
mess=raw_input("ENTER YOUR MESSAGE==> ")
def sending():
    emailserver=smtplib.SMTP("smtp.gmail.com",587)
    emailserver.starttls()
    emailserver.login(email,passw)
    emailserver.sendmail(email,sendmaili,mess)
    emailserver.quit()
    print("MESSAGE-SEND!")
sending()

