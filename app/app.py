import database.MyDB as mydb
import MyMods.settings as mod


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
                elif doit == "3":
                    print("Seçildi: ", doit)
                elif doit == "4":
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
                elif doit == "5":
                    print("Seçildi: ", doit)
                elif doit == "6":
                    print("Seçildi: ", doit)
                elif doit == "7":
                    print("Seçildi: ", doit)
                elif doit == "8":
                    self.user.newTable()
                elif doit == "9":
                    print("Seçildi: ", doit)
                elif doit == "10":
                    print("Seçildi: ", doit)
                elif doit == "11":
                    print("Seçildi: ", doit)
                else:
                    pass
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

    def newSubUser(self):
        pass

    def editSubUser(self):
        pass

    def deleteSubUser(self):
        pass

    def newTable(self):
        pass

    def switchTable(self):
        pass

    def deleteTable(self):
        pass

    def showChangeLog(self):
        pass
