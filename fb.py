
import pyrebase

class FIREBASE:
    config = {
        "apiKey": "AIzaSyAFacxjOfDEWwXv8JXAa9QORv7qUVu69Uk",
        "authDomain": "slambook-ab84c.firebaseapp.com",
        "databaseURL": "https://slambook-ab84c.firebaseio.com",
        "projectId": "slambook-ab84c",
        "storageBucket": "slambook-ab84c.appspot.com",
        "serviceAccount": "slambookfb.json"
    }
    def __init__(self):
        firebase_storage = pyrebase.initialize_app(config=self.config)
        self.storage = firebase_storage.storage()

    def upload(self, filename):
        self.storage.child(filename).put(filename)

    def download(self, filename):
        self.storage.child(filename).download(filename)
