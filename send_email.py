import smtplib, ssl

def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "" # write Your gmail address inside the Quotes
    password = "" # Put the password of gmail inside the Quotes

    receiver = "" # Put the receiver gmail address inside the Quotes
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host,port,context=context) as server:
        server.login(username,password)
        server.sendmail(username,receiver,message)