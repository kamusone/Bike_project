'''
    *** AirParif Scrapping ***
    
Created on Mon Dec 21  

@author: Hacene N
 
    '''
    
    
from selenium import webdriver
import time
import pandas as pd 
import numpy as np


path = "/home/fitec/Bureau/Formation_ABD/2. Data scrapping/chromedriver"
driver = webdriver.Chrome(path)

path_airParif = "https://www.airparif.asso.fr/stations#"
driver.get(path_airParif)  


### Récuperer les noms des stations
###################################
Stations = driver.find_elements_by_xpath("//select[@id='choixstation']")
station_name = ""

for st in Stations :
    station_name +=  st.text

station_name = station_name.split('\n')
station_name = station_name[1:]
time.sleep(2)



### Récuperer l'adresse des stations 
####################################

station_code = ["ARG", "AUB", "ARGENT", "A1", "ELYS", "BOB", "BAGNEA","HAUS", "AUT",
                "BP_EST", "SOULT", "CERGY", "CHAMP", "EVRY", "GEN", "GON", "DEF", "ULIS",
                "LOGNES", "LIMAY", "MANT", "MELUN", "MONTG", "NEUIL", "NOGENT", 
                "PA12", "PA13", "PA18", "PA01H", "PA07", "BASCH", "OPERA", "POMMEU", 
                "CELES", "RD7-C", "RD934", "RN13-G", "RN20-R", "RN20", "RN4-C", "RAMBO",
                "RN6", "RN2", "BONAP", "STDEN", "TREMB", "EIFF3", "VILLEM", "VITRY", "RUR_S", 
                "RUR-E", "RUR_N", "RUR-NE", "RUR-NO", "RUR-SE", "RUR-SO"]

station_adress = []
for code in station_code:
    
    path_airParif = "https://www.airparif.asso.fr/stations#" + code
    driver.get(path_airParif)     

    time.sleep(1)
    Adresses = driver.find_elements_by_xpath("//*[@id='info-station']/div/div[2]")
    station_adress.append(Adresses[0].text)
    
driver.quit()




### mettre l'adresse sur une seule ligne
''' '''
new_adress = []
for ad in station_adress :
    new_ad = ad.split("\n")
    new_adress.append(new_ad[0] + " " + new_ad[1])

data =[station_code, station_name, new_adress]
data = np.transpose(data)
stations_data = pd.DataFrame(data, columns = ["station_code", "station_name", "station_adress"])
stations_data.to_csv("stations_data.csv", index=False)



### Créer un filtre pour récuperer les stations qui sont dans Paris
''' '''
mask = []
for ad in new_adress :
    mask.append("750" in ad) 
    
stations_paris = data[mask]



### Créer un dataframe et sauvegarder le résultat en fichier .csv
''' '''
stations_paris = pd.DataFrame(stations_paris, columns = ["station_code", "station_name", "station_adress"])
stations_paris.to_csv("stations_paris.csv", index=False)

 