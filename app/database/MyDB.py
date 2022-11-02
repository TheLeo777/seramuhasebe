import time

import pymysql


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

    def register(self, email, username, password):
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

    def login(self):
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
            user = User(id, email, username, password, permission, settings, description)

            if permission == "developer":
                print("geliştirici modu")
            else:
                dbname = email.split('@')
                dbname = dbname[0] + "#" + dbname[1] + "_" + username

                userdb = UserDB(dbname, user)
                return True, user, userdb
        else:
            print("data yok")
            return False


class User:
    def __init__(self, id, email, username, password, permission, settings, description):
        self.USER_ID = id
        self.USER_EMAIL = email
        self.USER_USERNAME = username
        self.USER_PASSWORD = password
        self.USER_PERMISSION = permission
        self.USER_SETTINGS = settings
        self.USER_DESCRIPTION = description


class UserDB:
    def __init__(self, database, user):
        self.HOST = "localhost"
        self.USER = "root"
        self.PASSWORD = ""
        self.DATABASE = database

        self.user_permission = user.USER_PERMISSION

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

        if self.user_permission == "subuser":
            pass
        elif self.user_permission == "user":
            try:
                qstr1 = " SELECT * FROM cuts "
                self.cursor.execute(qstr1)
                table = self.cursor.fetchone()
            except pymysql.err.ProgrammingError:
                qstr2 = " CREATE TABLE IF NOT EXISTS cuts ( ID INT AUTO_INCREMENT NOT NULL, date varchar(255) NOT NULL," \
                        " count int NOT NULL, first_kilo int NOT NULL, second_kilo int NOT NULL," \
                        " first_price float NOT NULL, second_price float NOT NULL, first_income int NOT NULL," \
                        " second_income int NOT NULL, total_income int NOT NULL, PRIMARY KEY (ID) ) "
                self.cursor.execute(qstr2)
                self.conn.commit()
                print(f"{self.DATABASE} veritabanında tablo oluşturuldu.", qstr2)
        else:
            print("UserDB tablo kontrolünde hata")

    def new_cut(self):
        date = input("Tarih: ")
        str_count = input("Dal sayısı: ")
        count = int(str_count)
        first_kilo = input("Birinci Kilo: ")
        second_kilo = input("İkinci Kilo: ")
        str_first_price = input("Birinci Fiyatı: ")
        first_price = float(str_first_price)
        second_price = float(first_price / 2)
        first_income = int(first_kilo) * float(first_price)
        second_income = int(second_kilo) * float(second_price)
        total_income = first_income + second_income

        qstr1 = " SELECT * FROM cuts WHERE date = '{}' "
        qstr1 = qstr1.format(date)
        self.cursor.execute(qstr1)
        date_exists = self.cursor.fetchone()

        if date_exists:
            print("Bu tarihle bir kayıt mevcut.")
        else:
            qstr2 = " INSERT INTO `cuts` (`date`, `count`, `first_kilo`, `second_kilo`, `first_price`," \
                    " `second_price`,`first_income`, `second_income`, `total_income`) VALUES " \
                    "('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}') "

            qstr2 = qstr2.format(date, count, first_kilo, second_kilo, first_price, second_price, first_income, second_income, total_income)
            self.cursor.execute(qstr2)
            self.conn.commit()
            print("Kesim kaydedildi", qstr2)

    def showAllData(self):
        qstr1 = " SELECT * FROM cuts "
        self.cursor.execute(qstr1)
        data = self.cursor.fetchall()

        counter = 0
        count_total = 0
        firstkilo_total = 0
        secondkilo_total = 0
        income_total = 0

        print(50*'#')
        for i in data:
            counter = counter++1
            a = int(i[0])
            b = i[1]
            c = int(i[2])
            d = int(i[3])
            e = int(i[4])
            f = float(i[5])
            g = float(i[6])
            h = int(i[7])
            j = int(i[8])
            k = float(i[9])

            count_total += int(i[2])
            firstkilo_total += int(i[3])
            secondkilo_total += int(i[4])
            income_total += float(i[9])

            table = "ID: {} \n Tarih: {} \n Dal Sayısı: {} \n Birinci Kilo: {} \n İkinci Kilo: {} \n " \
                    "Birinci Fiyat: {} \n İkinci Fiyat: {} \n Birinci Gelir: {} \n İkinci Gelir: {} \n Toplam Gelir: {}"
            table = table.format(a,b,c,d,e,f,g,h,j,k)
            print(50*'#')
            print(table)
            print(50*'#')
            print('\n')
            totals = " Toplam Dal: {} || Toplam Birinci: {} \n Toplam İkinci: {} || Toplam Gelir: {} "
            totals = totals.format(count_total, firstkilo_total, secondkilo_total, income_total)
            print(50*'#')
            print(totals)
            print(50*'#')
            print('\n')
        print(f"{counter} adet kayıt bulundu.")

    def showData(self):
        print("""
        Arama yapmak için tarih formatları;
        
        GG/AA/YYYY
        AA/YYYY
        YYYY
        
        bu formatlar haricinde yapılan aramalar bir sonuç göstermeyecektir.
        """)
        time.sleep(2)
        date = input("Tarih girin: ")

        qstr1 = " SELECT * FROM cuts WHERE date LIKE '%{}' "
        qstr1 = qstr1.format(date)
        self.cursor.execute(qstr1)
        data = self.cursor.fetchall()

        if data:
            counter = 0
            count_total = 0
            firstkilo_total = 0
            secondkilo_total = 0
            income_total = 0

            print(50 * '#')
            for i in data:
                counter = counter++1
                a = int(i[0])
                b = i[1]
                c = int(i[2])
                d = int(i[3])
                e = int(i[4])
                f = float(i[5])
                g = float(i[6])
                h = int(i[7])
                j = int(i[8])
                k = float(i[9])

                count_total += int(i[2])
                firstkilo_total += int(i[3])
                secondkilo_total += int(i[4])
                income_total += float(i[9])

                table = "ID: {} \n Tarih: {} \n Dal Sayısı: {} \n Birinci Kilo: {} \n İkinci Kilo: {} \n " \
                        "Birinci Fiyat: {} \n İkinci Fiyat: {} \n Birinci Gelir: {} \n İkinci Gelir: {} \n Toplam Gelir: {}"
                table = table.format(a, b, c, d, e, f, g, h, j, k)
                print(50 * '#')
                print(table)
                print(50 * '#')
                print('\n')
                totals = " Toplam Dal: {} || Toplam Birinci: {} \n Toplam İkinci: {} || Toplam Gelir: {} "
                totals = totals.format(count_total, firstkilo_total, secondkilo_total, income_total)
                print(50 * '#')
                print(totals)
                print(50 * '#')
                print('\n')
            print(f"{counter} adet kayıt bulundu.")

        else:
            print("Bu tarihte bir kayıt bulunamadı.")

