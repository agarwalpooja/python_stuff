import imapclient
imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
imapObj.login('poojaag1606@gmail.com ', '9861867409')
imapObj.select_folder('INBOX')
# UIDs = imapObj.search(['SINCE 05-Jul-2018'])
import imaplib
imaplib._MAXLINE = 10000000
UIDs = imapObj.gmail_search('me')
rawMessages = imapObj.fetch(UIDs[0], ['BODY[]'])
import pprint
pprint.pprint(rawMessages)

import pyzmail
message = pyzmail.PyzMessage.factory(rawMessages[UIDs[0]][b'BODY[]'])
message.get_subject()
message.get_addresses('from')
message.get_addresses('to')
message.get_addresses('cc')
message.get_addresses('bcc')

if message.text_part != None:
    message.text_part.get_payload().decode(message.text_part.charset)
if message.html_part != None:
    message.html_part.get_payload().decode(message.html_part.charset)

imapObj.delete_messages(UIDs[0])
imapObj.expunge()
imapObj.logout()

