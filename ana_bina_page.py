from bs4 import BeautifulSoup as bs

class AnaBinaPage():

    def __init__(self,driver):

        self.driver = driver

        def return_css(which):

            return 'a[data-building="%s"][data-level-next]' % (which)

        self.ana_bina_click = return_css('main')

        self.heykel_click = return_css('statue')
        
        self.ciftlik_click = return_css('farm')

        self.kisla_click = return_css('barracks')

        self.gizli_depo_click = return_css('hide')

        self.pazar_click = return_css('market')

        self.ictima_meydani_click = return_css('place')

        self.depo_click = return_css('storage')

        self.demir_madeni_click = return_css('iron')

        self.oduncu_click = return_css('wood')

        self.kil_ocagi_click = return_css('stone')
    
        self.sur_click = return_css('wall')

        self.d_seviyeler = {}

        self.d_ihtiyaclar = {}

    def info(self):

        soup = bs(self.driver.page_source)

    def seviye_check(self):

        seviyes = [el.text[-1] for el in self.driver.find_elements_by_css_selector("table#buildings>tbody tr>td:nth-child(1)>span")]

        names = [el.get_attribute('id').split('_')[-1] for el in self.driver.find_elements_by_css_selector("table#buildings>tbody tr")[1:]]

        
        for c in range(len(seviyes)):
            
            self.d_seviyeler.update({names[c]:seviyes[c]})

        print(self.d_seviyeler)

    def ihtiyac_check(self):

        names = [el.get_attribute('id').split('_')[-1] for el in self.driver.find_elements_by_css_selector("table#buildings>tbody tr")[1:]]

        costs = self.driver.find_elements_by_css_selector("table#buildings>tbody tr td[class^='cost']")

        for c in range(len(names)):

            self.d_ihtiyaclar.update({names[c]:[costs[c].get_attribute('data-cost'),costs[c+1].get_attribute('data-cost'),costs[c+2].get_attribute('data-cost')]})
            
        print(self.d_ihtiyaclar)
        
