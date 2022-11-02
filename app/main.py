import time
import MyMods.settings as mod
from database.MyDB import MyDB  #, User


class App:
    def __init__(self, user, userdb):
        self.db = MyDB()
        self.db.connect()

        self.userdb = userdb

        self.user = user
        self.user_permission = self.user.USER_PERMISSION

    def start(self):
        while True:
            if self.user_permission == "subuser":
                print(mod.subuser_menu)

                doit = input("İşlem numarası girin: ")

                if doit == "0":
                    break
                elif doit == "1":
                    print("Seçildi: ", doit)
                    self.showAllData()
                elif doit == "2":
                    print("Seçildi: ", doit)
                    self.new_cut()
                else:
                    print("Geçersiz işlem")

            elif self.user_permission == "user" or "developer":
                print(mod.user_menu)

                doit = input("İşlem numarası girin: ")

                if doit == "0":
                    break
                elif doit == "1":
                    print("Seçildi: ", doit)
                    self.showAllData()
                elif doit == "2":
                    print("Seçildi: ", doit)
                    self.new_cut()
                elif doit == "3":
                    print("Seçildi: ", doit)
                    self.showData()
                elif doit == "4":
                    print("Seçildi: ", doit)
                else:
                    print("Geçersiz işlem")
            else:
                print("Devam etmek için gerekli yetkiye sahip değilsin!")
                break

    def showAllData(self):
        self.userdb.showAllData()

    def showData(self):
        self.userdb.showData()

    def new_cut(self):
        self.userdb.new_cut()

    def edit(self):
        pass

    def delete(self):
        pass


print(mod.starting_motd)
time.sleep(2)
mod.clear()

while True:
    db = MyDB()
    db.connect()
    haveAccount = input("Mevcut bir hesabınız yok ise 'Q' yazarak yeni bir hesap oluşturabilirsiniz. "
                        "Mevcut hesabınız ile giriş yapmak için 'Enter' basarak devam ediniz.")

    if haveAccount == "Q":
        print("Bilgilerinizi dikkatle giriniz.")
        time.sleep(3)
        mod.clear()
        while True:
            email = input("Email: ")
            username = input("Kullanıcı adı: ")
            password = input("Şifre: ")
            mailCheck = db.register(email, username, password)

            if mailCheck == True:
                print("kayıt başarılı.")
                break
            elif mailCheck == False:
                print("mail mevcut")
            else:
                print("hata")
        time.sleep(4)
        mod.clear()

        while True:
            auth, user, userdb = db.login()
            if auth:
                if user:
                    app = App(user, userdb)
                    app.start()
                    break
            else:
                continue
        break
    else:
        auth, user, userdb = db.login()
        if auth:
            if user:
                app = App(user, userdb)
                app.start()
                break
        else:
            continue
