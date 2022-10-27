import pymysql
import User as userr
import UserDB as userdb


class MyDB:
    def __init__(self):
        self.HOST = "localhost"
        self.USER = "root"
        self.PASSWORD = ""
        self.DATABASE = "MyDB"

    def connect(self):

        try:
            self.conn = pymysql.connect(
                host=self.HOST,
                user=self.USER,
                password=self.PASSWORD,
                database=self.DATABASE
            )

            self.cursor = self.conn.cursor()

        except:
            print("Veritabanına bağlanırken hata. Lütfen veritabanının oluşturulduğundan emin olun.")

        try:
            cstr1 = "CREATE DATABASE IF NOT EXISTS MyDB"
            self.cursor.execute(cstr1)
            db = self.cursor.fetchone()
        except:
            print("Veritabanı oluşturulurken bir hata oluştu.")

        try:
            cstr2 = "SELECT * FROM `users`"
            self.cursor.execute(cstr2)
            table = self.cursor.fetchone()
        except pymysql.err.ProgrammingError:
            qstr1 = "CREATE TABLE IF NOT EXISTS `users` (ID INT AUTO_INCREMENT NOT NULL, email varchar(255) NOT NULL," \
                    " username varchar(255) NOT NULL, password varchar(255) NOT NULL, permission varchar(255)," \
                    " settings varchar(1000), description varchar(1000), PRIMARY KEY (ID))"
            self.cursor.execute(qstr1)
            print("Tablo oluşturuldu. \n", qstr1)

            qstr2 = " INSERT INTO `users`(`email`, `username`, `password`, `permission`, `settings`, `description`) VALUES " \
                    "('admin','admin','admin','developer','none','none') "
            self.cursor.execute(qstr2)
            self.conn.commit()
            print("Geliştirici hesabı oluşturuldu", qstr2)

        print("Veritabanı bağlantısı kuruldu.")

    def _register(self, email, username, password):
        cstr1 = "SELECT * FROM `users` WHERE email = '{}'"
        cstr1 = cstr1.format(email)
        self.cursor.execute(cstr1)
        data = self.cursor.fetchone()

        if data:
            print("email exists")
            return False
        else:
            cstr2 = " INSERT INTO `users`(`email`, `username`, `password`, `permission`, `settings`, `description`) VALUES " \
                    "('{}','{}','{}','{}','{}','{}') "
            cstr2 = cstr2.format(email, username, password, "user", "none", "none")
            self.cursor.execute(cstr2)
            self.conn.commit()

            mail = email.split('@')
            mail = mail[0] + "#" + mail[1]
            cstr3 = """ CREATE DATABASE IF NOT EXISTS `{}_{}` """
            cstr3 = cstr3.format(mail, username)
            self.cursor.execute(cstr3)
            print("Kullanıcı database'i oluşturuldu: ", cstr3)
            print("kayıt yapıldı")
            return True

    def _login(self):
        email = input("Email: ")
        password = input("Şifre: ")

        cstr1 = """ SELECT * FROM users WHERE email ='{}' AND password ='{}' """
        cstr1 = cstr1.format(email, password)
        self.cursor.execute(cstr1)
        self.conn.commit()
        data = self.cursor.fetchone()

        if data:
            print("Kullanıcının verileri: ", data)
            id = data[0]
            email = data[1]
            username = data[2]
            password = data[3]
            permission = data[4]
            settings = data[5]
            description = data[6]
            user = userr.User(id, email, username, password, permission, settings, description)

            if permission == "developer":
                print("geliştirici modu")
            else:
                dbname = email.split('@')
                dbname = dbname[0] + "#" + dbname[1] + "_" + username

                userdb.UserDB(dbname)
            return True, user
        else:
            print("data yok")
            return False
