class User:
    _email = ""
    _password = ""

    def email(self):
        return self._email

    def password(self):
        return self._password

    def set_email(self, value):
        self._email = value

    def set_password(self, value):
        self._password = value
