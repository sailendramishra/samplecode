# -*- coding: utf-8 -*-
"""
@author: Sailendra

"""
# -*- coding: utf-8 -*-
import os as os
import pandas as pd
import datetime as dt
import numpy as np
import sys
import glob
from bs4 import BeautifulSoup  # HTML data structure
import urllib.request 

if __name__ == '__main__':
    
    ## Working Folder Set
    dirVal = r"C:\Users\Admin\Desktop\python\Webscrapping" 
    os.chdir(dirVal) 
    
    curUrl = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
    
    varHTML = None
    
    ## Reading content from url and stored in html (variable)
    with urllib.request.urlopen(curUrl) as response:
        varHTML = response.read()

    ## Convert to beautiful object lxml parsing
    htmlSoup = BeautifulSoup(varHTML, "lxml") 
    
    ## Get the table 
    top250HtmlTable = htmlSoup.find('table', attrs={'data-caller-name':"chart-top250movie"})
    
    ## Get the table body
    tableBody = top250HtmlTable.find('tbody', attrs={'class':"lister-list"})
    
    ## Get the rows 
    tableRows = tableBody.findAll("tr")
    
    ## Should be 250 rows 
    print(len(tableRows))
    
    titlenurlList = []
    
    for row in tableRows:
        cols = row.findAll("td")
        ## title columns
        titleCol = cols[1]
        ## rating columns
        ratingCol = cols[2]
        
        ## find href link 
        titleHref = titleCol.find("a")
        ## Get title Name
        titleName = titleHref.get_text()
        
         ## Get url of the title
        titleLink = "https://www.imdb.com"+ titleHref["href"]
        titaleRating = ratingCol.get_text().replace("\n", "")
        
        titlenurlList.append({"Title": titleName, "Url":titleLink, "Rating": titaleRating })
        
    ## Convert to data frame
    movieDF = pd.DataFrame(titlenurlList)
    
    ## Save as CSV
    movieDF[["Title","Rating", "Url"]].to_csv("IMDB_top_250.csv", index =False)
 
