import datetime

############ + Settings + ############

# MOTD SETTINGS
motd_stars = 40

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# DATE & TIME FORMAT

dt = datetime.datetime.now()
datetime = dt.strftime("%d/%m/%Y, %H:%M:%S")

############ - Settings - ############


# CLEAR CONSOLE SCREEN
def clear():
    print(100*"\n")


# MOTD STRING
starting_motd = motd_stars * f"{bcolors.OKCYAN}*{bcolors.ENDC}" + "\n" + f"{bcolors.OKGREEN}Hoşgeldiniz" + \
                "\n" +  f"Tarih ve Saat: {datetime} {bcolors.ENDC}" +  "\n" + motd_stars * f"{bcolors.OKCYAN}*{bcolors.ENDC}"


# APP MENU BY PERMISSIONS

subuser_menu = """
                    ############### IŞLEMLER ###############
                    #
                    # 1-) Kayıtları Gör
                    # 2-) Kayıtları Gör (Tarih)
                    # 3-) Yeni Kayıt Ekle
                    # 4-) Alacak/Verecek Gör
                    #
                    # 0-) Çıkış
                    #
                    ########################################
                    """

user_menu = """
                    ############### IŞLEMLER ###############
                    #
                    # 1-) Kayıtları Gör
                    # 2-) Kayıtları Gör (Tarih)
                    # 3-) Yeni Kayıt Ekle
                    # 4-) Kayıt Düzenle
                    # 5-) Kayıt Sil
                    # 6-) Alacak/Verecek Gör
                    # 7-) Alacak/Verecek Ekle
                    # 8-) Alacak/Verecek Düzenle
                    # 9-) Alacak/Verecek Sil
                    #
                    # 0-) Çıkış
                    #
                    ########################################
                    """



