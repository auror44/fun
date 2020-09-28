class MainPage():

    def __init__(self):

        def return_css(which):
            
            beg = "div.visual-label.visual-label-"

            end = ".tooltip-delayed"

            return beg+which+end

        self.ana_bina = return_css('main')

        self.ciftlik = return_css('farm')

        self.kisla = return_css('barracks')

        self.gizli_depo = return_css('hide')

        self.pazar = return_css('market')

        self.ictima_meydani = return_css('place')

        self.depo = return_css('storage')

        self.demir_madeni = return_css('iron')

        self.oduncu = return_css('wood')

        self.kil_ocagi = return_css('stone')
    
        
