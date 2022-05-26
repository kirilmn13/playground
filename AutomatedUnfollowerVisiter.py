# %%
from instapy import InstaPy
import instaloader
from instapy.util import get_number_of_posts 
from Scrapper import instagram
import requests
import json
from bs4 import BeautifulSoup
import re
import pandas as pd 
from colorthief import ColorThief
import colorsys
import time
import pandas as pd
import json
import random
import tkinter as tk
import os
# %%

browser = r"C:\Program Files\Mozilla Firefox\firefox.exe"
usuario = "kirilmbphoto"
contraseña = "fikukan7"
sesion = InstaPy(username=usuario, password=contraseña,browser_executable_path=browser)
sesion.login()
            
#Quitar GECKODRIVER de tareas si no funciona


# %%

ig = instagram("kirilmbphoto", "fikukan7")     #Se define la sesión con contraseña y cuenta
ig.login()    
ig.gohref("https://www.instagram.com/lightartsalicante/")




#%%

LOC = "C:/Users/Kiril/InstaPy/logs/lightartsalicante/relationship_data/kirilmbphoto/nonfollowers/13-02-2021~[1330-1631]~630.json"
with open(LOC) as f:
  unfollowers = json.load(f)


dataframe = pd.DataFrame(unfollowers) #Convertimos objeto Json a Dataframe de pandas
dataframe.shape  #Comprobarmos la forma del dataframe
dataframe = dataframe.iloc[:,0].astype(str) #Convertimos todos los objeros del dataframe en strings
type(dataframe[8]) #Comprobamos que estamos trabajando con Strings




#%%



### Bucle para visitar las paginas de los no seguidores 

dataframe.shape 

for index, number in dataframe.iteritems():
  print(dataframe[index])
  user = dataframe[index]
  n = random.randint(10,15)
  time.sleep(n)
  ig.gouser(user)
  dataframe = dataframe.drop(index=index)
  input("Press Enter to continue...")


#%%
dataframe.to_csv('loquequeda.csv')


#%%
