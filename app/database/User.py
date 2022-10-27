class User:
    def __init__(self, id, email, username, password, permission, settings, description):
        self.USER_ID = id
        self.USER_EMAIL = email
        self.USER_USERNAME = username
        self.USER_PASSWORD = password
        self.USER_PERMISSION = permission
        self.USER_SETTINGS = settings
        self.USER_DESCRIPTION = description

    def newTable(self):
        pass

    def newSubUser(self):
        pass

    # Kullanıcının yapabileceği işlemler/fonksiyonlar buraya yazılacak.ß
