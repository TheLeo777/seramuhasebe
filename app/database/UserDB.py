import pymysql


class UserDB:
    def __init__(self, database):
        self.HOST = "localhost"
        self.USER = "root"
        self.PASSWORD = ""
        self.DATABASE = database

        try:
            self.conn = pymysql.connect(
                host=self.HOST,
                user=self.USER,
                password=self.PASSWORD,
                database=self.DATABASE
            )

            self.cursor = self.conn.cursor()

            print(f"Kullanıcı {self.DATABASE} veritabanına bağlandı")

        except:
            print("UserDB bağlanırken bir hata oluştu.")

    def createTable(self):
        pass
