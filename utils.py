import json
import os
import smtplib


class UTILS:

    _sender_email = 'tharuneshwar27@gmail.com'
    _sender_pass = 'tharun sendhil'
    _receiver_email = _sender_email
    
    def __init__(self, username, data):
        self._data = data
        self._username = username

    def _Mail(self):#message):
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(self._sender_email, self._sender_pass)
        text = str(self._data)
        s.sendmail(self._sender_email, self._sender_email, text)
        s.quit()

    def run(self):
        self._Mail()
