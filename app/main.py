import time
import MyMods.settings as mod
import database.MyDB as mydb

class App:
    def __init__(self, user):
        self.db = mydb.MyDB()
        self.db.connect()

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
                elif doit == "2":
                    print("Seçildi: ", doit)
                else:
                    print("Geçersiz işlem")

            elif self.user_permission == "user" or "developer":
                print(mod.user_menu)

                doit = input("İşlem numarası girin: ")

                if doit == "0":
                    break
                elif doit == "1":
                    print("Seçildi: ", doit)
                elif doit == "2":
                    print("Seçildi: ", doit)
                elif doit == "3":
                    print("Seçildi: ", doit)
                elif doit == "4":
                    print("Seçildi: ", doit)
                else:
                    print("Geçersiz işlem")
            else:
                print("Devam etmek için gerekli yetkiye sahip değilsin!")
                break

    def showAllData(self):
        pass

    def addNew(self, a, b, c, d, x1, x2, y1, y2, z):
        pass

    def edit(self):
        pass

    def delete(self):
        pass


print(mod.starting_motd)
time.sleep(5)
mod.clear()

while True:
    db = mydb.MyDB()
    db.connect()
    haveAccount = input("Mevcut bir hesabınız yok ise 'Q' yazarak yeni bir hesap oluşturulabilirsiniz. Mevcut hesabınız ile giriş yapmak için 'Enter' basarak devam ediniz.")
    "asdasd"
    if haveAccount == "Q":
        print("Bilgilerinizi dikkatle giriniz.")
        time.sleep(5)
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
        time.sleep(7)
        mod.clear()

        while True:
            auth, user = db.login()
            if auth == True:
                if user:
                    app = App(user)
                    app.start()
                    break
            else:
                continue
        break
    else:
        auth, user = db.login()
        if auth == True:
            if user:
                app = App(user)
                app.start()
                break
        else:
            continue



