#Important Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn import metrics
from sklearn.metrics import classification_report
import csv
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

url = 'https://libyanclinic.online/'

options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome('chromedriver.exe')
driver.get(url)

driver.find_element(By.NAME,"username").send_keys("admin")

driver.find_element(By.NAME,"password").send_keys("admin")
driver.find_element(By.CLASS_NAME,"btnSubmit").click()

df = pd.DataFrame()

for x in range(1,132):
    driver.get(url+'precords/?page='+str(x))
    time.sleep(2)
    page_url=driver.page_source
    data = pd.read_html(page_url)
    #print(type(df1))
    df1 = pd.DataFrame(data[0])
    df=pd.concat([df,df1], ignore_index=True)
    

#Converting the Scrapped data into the Csv File
df.to_csv('data.csv')

#Importing the Csv File
records = pd.read_csv('data.csv')
records.head()

#Information of our data
records.info()    

#Checking Stats of the Data
records.describe()

#Checking if there is any missing or null values
records.isnull().sum()

#Checking the relation between Patients and thier ages
#Scatter Chart
plt.figure(figsize=(10,9)) 
plt.scatter(records[ 'Age'],records['Daily_PN'], color = 'green')
plt.xlabel("Age Of Patients" ,fontsize= 18)
plt.ylabel("Daily No Patients",fontsize= 18)
plt.show()


#Checking the no of patients vs the no of doctros needed
#Bar Chart
plt.figure(figsize=(20,10)) 
plt.bar(records['Daily_PN'], records['Doctor No.'])
plt.xlabel("Daily Patients" ,fontsize= 18)
plt.ylabel("Doctors Needed",fontsize= 18)
plt.show()

#Checking the no of patients vs the no of medicens needed
#Bar Chart
plt.figure(figsize=(10,9)) 
plt.bar(records['Daily_PN'], records['Medicine No.'], color='red')
plt.xlabel("Daily Patients" ,fontsize= 18)
plt.ylabel("Medicens Required",fontsize= 18)
plt.show()


#Relation between all the columns inside the data
plt.figure(figsize=(15,5))
p = sns.heatmap(records.corr(), annot=True,cmap ='RdYlGn')

