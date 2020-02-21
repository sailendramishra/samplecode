# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 01:10:35 2020

@author: Sailendra
"""
# -*- coding: utf-8 -*-
from bs4  import BeautifulSoup
import os as os
import pandas as pd
import datetime as dt
from datetime import timedelta
import numpy as np
import glob
from selenium import webdriver
import time
if __name__ == '__main__':
   
    dirVal = r'Y:\bitcoinservices'  
    os.chdir(dirVal) 

    ## Open a chrome browser
    chromDriver = webdriver.Chrome(r"Y:\bitcoinservices\code\old\chromedriver.exe")     
    
    curUrl = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
    
    ## Hit the url
    chromDriver.get(curUrl)
    ## Wait 5 seconds
    time.sleep(5)    
    varHTML = None
    varHTML = chromDriver.page_source
    ## Convert to beautiful object lxml parsing
    htmlSoup = BeautifulSoup(varHTML, "lxml") 
    
    ## find the url with pointing to text "The Good, the Bad and the Ugly"
    linkUrl = chromDriver.find_element_by_link_text("The Good, the Bad and the Ugly")
    ## got to the page
    linkUrl.click()
    ## Close the driver
    chromDriver.close()
