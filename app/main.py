import time
import MyMods.settings as mod
import database.MyDB as mydb
from app import App

print(mod.starting_motd)
time.sleep(5)
mod.clear()

while True:
    db = mydb.MyDB()
    db.connect()
    haveAccount = input("Mevcut bir hesabınız yok ise 'Q' yazarak yeni bir hesap oluşturulabilirsiniz. Mevcut hesabınız ile giriş yapmak için 'Enter' basarak devam ediniz.")

    if haveAccount == "Q":
        print("Bilgilerinizi dikkatle giriniz.")
        time.sleep(5)
        mod.clear()
        while True:
            email = input("Email: ")
            username = input("Kullanıcı adı: ")
            password = input("Şifre: ")
            mailCheck = db._register(email, username, password)

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
            auth, user = db._login()
            if auth == True:
                if user:
                    app = App(user)
                    app.start()
                    break
            else:
                continue
        break
    else:
        auth, user = db._login()
        if auth == True:
            if user:
                app = App(user)
                app.start()
                break
        else:
            continue










