from SeleniumTools import SeleniumTools
from main_page import MainPage
from ana_bina_page import AnaBinaPage
import time


class klanlar():
    def __init__(self):
        
        self.st = SeleniumTools("https://www.klanlar.org")

        self.main_page = MainPage()

        self.ana_bina_page = AnaBinaPage(self.st.driver)
        
    def info(self):

        self.username = "auror4"
        self.password = "izocam88"
        self.world = "61"
        
    def login_page(self):

        self.st.humantype("input#user",self.username) #Entering username
        self.st.humantype("input#password",self.password) #Entering password
        self.st.check("a.btn-login",'clicked') #Clicking Giris

        self.st.check("a.world-select[href$='"+self.world+"']>span",'clicked') #World is clicked

        try:

            self.st.check("a.popup_box_close.tooltip-delayed",'clicked') # Click pop-up if

        except Exception as error:
            print(error)
            print("No pop-up")

    def ana_bina_page_check(self):

        self.st.check('table#buildings','visible') #Did page load on ana bina 

    def check_mission(self):

        try:
            self.st.check('btn.btn-confirm-yes','clicked') #If mission pops up,click

        except Exception as e:

            print(e)
            print('Mission is not present')

        
        


bot = klanlar()

bot.info()
bot.login_page()
bot.st.check(bot.main_page.ana_bina,'clicked')
bot.ana_bina_page.seviye_check()
bot.ana_bina_page.ihtiyac_check()

with open('route.txt','r') as f:

    route = f.readlines()

    route = [el.strip() for el in route]
    print(route)
    
def _click(bot,which):
    bot.check_mission()
    while True:
        
        try:
            bot.st.check(which,'clicked')
            
            return
        except Exception as e:
            print(e)


    
for line in route:
    print(line)
    try:
        seviye = line.split("-")[-1]

    except:

        continue

    bot.ana_bina_page.seviye_check()

    if "ODUN" in line and int(seviye)<int(bot.ana_bina_page.d_seviyeler['wood']):
        
        _click(bot,bot.ana_bina_page.oduncu_click)

    elif "ANA" in line and int(seviye)<int(bot.ana_bina_page.d_seviyeler['main']):

        _click(bot,bot.ana_bina_page.ana_bina_click)

    elif "KISLA" in line and int(seviye)<int(bot.ana_bina_page.d_seviyeler['barracks']):

        _click(bot,bot.ana_bina_page.kisla_click)

    elif "CIFTLIK" in line and int(seviye)<int(bot.ana_bina_page.d_seviyeler['farm']):

        _click(bot,bot.ana_bina_page.ciftlik_click)
        
    elif "DEPO" in line and int(seviye)<int(bot.ana_bina_page.d_seviyeler['storage']):

        _click(bot,bot.ana_bina_page.depo_click)
        
    elif "KIL" in line and int(seviye)<int(bot.ana_bina_page.d_seviyeler['stone']):

        _click(bot,bot.ana_bina_page.kil_ocagi_click)

    elif "GIZLIDEPO" in line and int(seviye)<int(bot.ana_bina_page.d_seviyeler['hide']):

        _click(bot,bot.ana_bina_page.gizli_depo_click)
    
    
