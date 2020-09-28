from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox import options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.proxy import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import exceptions
from selenium.webdriver.common.action_chains import ActionChains
from time import time,sleep
from selenium.webdriver.chrome.options import Options
from datetime import datetime, timedelta
import sys
import string
import random
import os
class SeleniumTools():
    def __init__(self,url):

        path = './chromedriver'
        
        chrome_options = Options()
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")

        self.driver = webdriver.Chrome(executable_path=path,chrome_options=chrome_options)
        self.driver.get(url)
        # self.driver.maximize_window() 
        
    def check(self,css,ch):
        
        w=WebDriverWait(self.driver,5)

        if ch == 'click':
        
            w.until(EC.element_to_be_clickable((By.CSS_SELECTOR,css)))
        
        elif ch == 'visible':
        
            w.until(EC.visibility_of_element_located((By.CSS_SELECTOR,css)))
        
        elif ch == 'xclick' :
        
            w.until(EC.element_to_be_clickable((By.XPATH,css)))
        
        elif ch == 'xvisible':
            
            w.until(EC.visibility_of_element_located((By.XPATH,css)))
        

        elif ch == 'clicked':
            
            w.until(EC.element_to_be_clickable((By.CSS_SELECTOR,css)))
            self.scrollLoc(css,'','css')
            self.driver.find_element_by_css_selector(css).click()
        
        elif ch == 'xclicked':
           
            w.until(EC.element_to_be_clickable((By.XPATH,css)))
            self.scrollLoc(css,'','xpath')
            self.hover(css,'')
            self.driver.find_element_by_xpath(css).click()
        
        elif type(ch) is int: #If xpath
            
            w.until(EC.element_to_be_clickable((By.XPATH,css)))
            self.scrollLoc(css,'','xpath')
            self.driver.find_elements_by_xpath(css)[ch].click()

        elif type(ch) is float: #If Css, give css as 0.1,1.1 etc.

            ch=round(ch)
            w.until(EC.element_to_be_clickable((By.CSS_SELECTOR,css)))
            self.scrollLoc(css,'','css')
            self.driver.find_element_by_css_selector(css)[ch].click()            
    
        
    def hover(self,css,status):
        
        print('---hover---')
        print(css)
        self.wait(css,'xvisible')
        #self.scrollLoc(css,status,'xpath')
        if status=='':
            el=self.driver.find_element_by_xpath(css)
        else:
            el=self.driver.find_elements_by_xpath(css)[status]
       
        hover = ActionChains(self.driver)
        hover.move_to_element(el)
        self.randomWait()
        print('moving')
        print(status)
        if status!=0:
            print('Click')
            #hover.click() 
        
        hover.perform()    
        self.randomWait()
    
    def hoverEl(self,el):
        hover = ActionChains(self.driver)
        hover.move_to_element(el)
        self.randomWait()
        hover.click()
        hover.perform()
        self.randomWait()
        


    def scrollLoc(self,cssclick,c,typ):
            
        timer=time()
        
        
        while not self.element_in_viewport(cssclick,c,typ) and not time()-timer>10:
            
            if type(c) is int and typ=='css':
                
                print('--scroll---')
                
                self.driver.execute_script('arguments[0].scrollIntoView({behavior: "smooth", block: "center"})', self.driver.find_elements_by_css_selector(cssclick)[c] ) 

            elif type(c) is int and typ=='xpath':
                
                print('--scroll---')
                
                self.driver.execute_script('arguments[0].scrollIntoView({behavior: "smooth", block: "center"})', self.driver.find_elements_by_xpath(cssclick)[c] ) 
                
            elif typ=='css':
                
                print('--scroll---')

                self.driver.execute_script('arguments[0].scrollIntoView({behavior: "smooth", block: "center", inline: "center"})', self.driver.find_element_by_css_selector(cssclick) )
            elif typ=='xpath':
                print('--scroll---')

                self.driver.execute_script('arguments[0].scrollIntoView({behavior: "smooth", block: "center", inline: "center"})', self.driver.find_element_by_xpath(cssclick))
            
            elif typ == 'el':
                print('--scroll---')
                self.driver.execute_script('arguments[0].scrollIntoView({behavior: "smooth", block: "center", inline: "center"})', cssclick)

                
    def screenSize(self):
        a = self.driver.execute_script("return outerWidth")
        c = self.driver.execute_script("return outerHeight - innerHeight")
        b = self.driver.execute_script("return outerHeight")
    
    def element_in_viewport(self,css,status,typ):
        if typ=='css' and type(status) is int:
            elem=self.driver.find_elements_by_css_selector(css)[status]
        elif typ=='xpath' and type(status) is int:
            elem=self.driver.find_elements_by_xpath(css)[status]
        elif typ=='css':
            elem=self.driver.find_element_by_css_selector(css)
        elif typ=='xpath':
            elem=self.driver.find_element_by_xpath(css)
        elif typ == 'el':
            elem = css
        elem_left_bound = elem.location.get('x')
        elem_top_bound = elem.location.get('y')
        elem_width = elem.size.get('width')
        elem_height = elem.size.get('height')
        elem_right_bound = elem_left_bound + elem_width
        elem_lower_bound = elem_top_bound + elem_height

        win_upper_bound = self.driver.execute_script('return window.pageYOffset')
        win_left_bound = self.driver.execute_script('return window.pageXOffset')
        win_width = self.driver.execute_script('return document.documentElement.clientWidth')
        win_height = self.driver.execute_script('return document.documentElement.clientHeight')
        win_right_bound = win_left_bound + win_width
        win_lower_bound = win_upper_bound + win_height

        return all((win_left_bound <= elem_left_bound,
                    win_right_bound >= elem_right_bound,
                    win_upper_bound <= elem_top_bound,
                    win_lower_bound >= elem_lower_bound)
                   )

    def randomScroll(self):
        try:
            for el in range(0,random.randint(1,4)):
                sc=random.random()*600
                self.driver.execute_script("window.scrollBy({top:"+str(sc)+",left: 0,behavior: 'smooth'});")
                self.randomWait()
        except:
            self.close('randomScroll error')
    def randomWait(self):
        sleep(random.randint(1,2))

    def humantype(self,css,word):

        el=self.driver.find_element_by_css_selector(css)
        letters=string.ascii_lowercase+string.digits
        for c in word:
            if c=='':
                break
            el.send_keys(c)
            sleep(random.uniform(0.3,0.4))
            if random.randint(0,6)==2:
                el.send_keys(letters[random.randint(0,len(letters)-1)])
                if random.randint(0,5)==2:
                    el.send_keys(letters[random.randint(0,len(letters)-1)])
                    sleep(random.uniform(0.3,0.8))
                    el.send_keys(Keys.BACKSPACE)
                    sleep(random.uniform(0.6,0.9))
                el.send_keys(Keys.BACKSPACE)
                sleep(random.uniform(0.6,0.9))
        self.randomWait()

