#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#importing the required libraries
import requests
from selenium import webdriver
from bs4 import BeautifulSoup as bs
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from tkinter import Tk


# In[ ]:


#initialise the web driver
browser = webdriver.Chrome(ChromeDriverManager().install())


# In[ ]:


#importing the input file for performing the task
post_urls = pd.read_csv(r"your file path goes here")
tourism_urls=post_urls["Post Url"].tolist()


# In[ ]:


#creating an empty list to append the outputs
post_url=[]
post_id=[]
post_timestamp=[]


# In[ ]:


#looping to pull the timestamp data using a site
for link_url in tourism_urls:
    browser.get("https://ollie-boyd.github.io/Linkedin-post-timestamp-extractor/")
    time.sleep(2)
    text_box=browser.find_element(By.XPATH,"//input[@id='url']")
    text_box.send_keys(link_url)
    
    get_timestamp=browser.find_element(By.XPATH,"//button[@onclick='getDate()']")
    get_timestamp.click()
    time.sleep(1)
    
    page_source_code = browser.page_source
    soup=bs(page_source_code,'lxml')
    get_date=soup.find('span',{'id':'date'})
    data=get_date.text

    post_url.append(link_url)
    index_link=tourism_urls.index(link_url)
    post_id.append(index_link)
    post_timestamp.append(data)
    print(data)
    print(link_url)
    print(index_link)
    time.sleep(1)
    
   


# In[ ]:


#creating a dataframe to append the appended list
data = {
    "Date Posted": post_url,
    "Date":post_id,
    "Media Type": post_timestamp,
}

df = pd.DataFrame(data)


# In[ ]:


#printing the top head of the output dataframe
df.head(30)


# In[ ]:


#exporting the output to the local machine
df.to_csv(r'/Users/rajkupekar/Desktop/Raj/ABP_Time.csv', index=False)


# In[ ]:





# In[ ]:





# In[ ]:




