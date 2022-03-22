import smtplib

def send_email(client_ip, gmail_sender, gmail_sender_pass, gmail_receiver, smtp_addr):
    sent_from = gmail_sender
    to = [gmail_receiver]
    email_text = "%s" % (client_ip)
   
    try:
        smtp_server = smtplib.SMTP_SSL(smtp_addr, 465)
        smtp_server.ehlo()
        smtp_server.login(gmail_sender, gmail_sender_pass)
        smtp_server.sendmail(sent_from, to, email_text)
        smtp_server.close()
        print ("Email sent successfully!")
    except Exception as ex:
        print ("Something went wrong",ex)
