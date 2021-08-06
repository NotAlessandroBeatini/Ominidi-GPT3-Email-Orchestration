import email
import imaplib

EMAIL = 'helpfromapes@gmail.com'
PASSWORD = '123456QWERTY!'
SERVER = 'imap.gmail.com'

mail = imaplib.IMAP4_SSL(SERVER)
mail.login(EMAIL, PASSWORD)
mail.select('inbox')

n=0
(retcode, messages) = mail.search(None, '(UNSEEN)')
if retcode == 'OK':

   for num in messages[0].split() :
      print('Processing ')
      n=n+1

      typ, data = mail.fetch(num,'(RFC822)')
      for response_part in data:
         if isinstance(response_part, tuple):
            original = email.message_from_bytes(response_part[1])
            raw_email = data[0][1]
            typ, data = mail.store(num,'+FLAGS','\\Seen')
            print("*"*8)
            raw_email_string = raw_email.decode('utf-8')
            email_message = email.message_from_string(raw_email_string)
            for part in email_message.walk():
               if part.get_content_type() == "text/plain":
                     body = part.get_payload(decode=True)
                     print("Body: \n\n%s" %(body.decode('utf-8')))
               else:
                     continue