import json
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

class UTILS:

    _sender_email = 'tharuneshwar27@gmail.com'
    _sender_pass = 'tharun sendhil'
    _receiver_email = _sender_email
    _filename = 'slambookdata.json'

    def __init__(self, data):
        self._data = data
        self._username = data['YourName']

    def _Store(self):
        json_object = json.dumps(self._data, indent=4)
        with open(self._filename, "w") as outfile:
            outfile.write(json_object)
        #self._MIME()

    def _MIME(self):
        message = MIMEMultipart()
        message['From'] = self._sender_email
        message['To'] = self._receiver_email
        message['Subject'] = f"This is From {self._username}."
        message.attach(MIMEText(self._username, 'plain'))
        attach_file_name = self._filename
        attach_file = open(attach_file_name, 'r')
        payload = MIMEBase('application', 'octate-stream')
        payload.set_payload((attach_file).read())
        encoders.encode_base64(payload)
        payload.add_header('Content-Decomposition', 'attachment', filename=attach_file_name)
        message.attach(payload)
        #self._Mail(message=message)

    def _Mail(self, ):#message):
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(self._sender_email, self._sender_pass)
        #text = message.as_string()
        s.sendmail(self._sender_email, self._sender_email, self._data)#text)
        #print('Mailed')
        s.quit()
        #os.remove(self._filename)

    def run(self):
        #self._Store()
        self._Mail()
