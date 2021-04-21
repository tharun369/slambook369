import json
from fb import FIREBASE

class UTILS:

    _sender_email = 'tharuneshwar27@gmail.com'
    _sender_pass = 'tharun sendhil'
    _receiver_email = _sender_email

    def __init__(self, username, data, app):
        self._data = data
        self._username = username
        self._app = app
        self._filename = f"{self._username}.json"

    def _Store(self):
        with open(self._filename, 'w') as jsn:
            json.dump(self._data, jsn,indent=4)
        jsn.close()
        fb = FIREBASE()
        fb.upload(self._filename)

    def run(self):
        self._Store()