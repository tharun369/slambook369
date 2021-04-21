from flask_mail import Mail, Message
import json

class UTILS:

    _sender_email = 'tharuneshwar27@gmail.com'
    _sender_pass = 'tharun sendhil'
    _receiver_email = _sender_email
    _filename = 'slambookdata.json'

    def __init__(self, username, data, app):
        self._data = data
        self._username = username
        self._app = app
        mail_settings = {
            "MAIL_SERVER": 'smtp.gmail.com',
            "MAIL_PORT": 587,
            "MAIL_USE_TLS": True,
            "MAIL_USE_SSL": False,
            "MAIL_USERNAME": self._sender_email,
            "MAIL_PASSWORD": self._sender_pass
        }
        self._app.config.update(mail_settings)
        self.mail = Mail(self._app)

    def _Mail(self):
        with self._app.app_context():
            msg = Message()
            msg.subject=f"Slam Book From ~ {self._username}"
            msg.sender=self._sender_email
            msg.recipients=[self._receiver_email]
            msg.body=f'From {self._username}, {self._data}'
            #with self._app.open_resource(self._filename) as fp:
                #msg.attach(f"{self._filename}", "application/json", fp.read())
            self.mail.send(msg)
            print('mailed')

    def run(self):
        self._Mail()()
