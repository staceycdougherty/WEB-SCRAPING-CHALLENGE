#!/usr/bin/env python
# coding: utf-8

# In[7]:


# Dependencies
from bs4 import BeautifulSoup as bs
import requests
import pymongo
from splinter import Browser
import pandas as pd
from flask import Flask, render_template
from webdriver_manager.chrome import ChromeDriverManager
import time


# In[10]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[11]:


#visit site
url = "https://redplanetscience.com/"
browser.visit(url)

time.sleep(1)


# In[12]:


# Scrape page into Soup
html = browser.html
soup = bs(html, "html.parser")
#soup


# In[13]:


# Get the news name
news_title = soup.find_all('div', class_='content_title')[0].text

# Get the news paragraph
news_p = soup.find_all('div', class_='article_teaser_body')[0].text
#print it out to see if it found it
#news_title
#news_p


# In[14]:


#visit site for picture
featured_image_url = "https://spaceimages-mars.com/"
browser.visit(featured_image_url)
    
time.sleep(1)
    
html = browser.html
soup = bs(html, "html.parser")
#soup


# In[15]:


relative_image_path = soup.find_all('img')[1]["src"]
featured_img_url = featured_image_url + relative_image_path
    
featured_img_url


# In[31]:


#mars facts scraping
mars_facts_url = 'https://galaxyfacts-mars.com/'
tables = pd.read_html(mars_facts_url)
#tables

table_df = pd.DataFrame(tables[1])
table_df.columns = ["Attributes", "Values"]
table_df.set_index("Attributes", inplace =True)
table_df
#convert to html table
html_table = table_df.to_html()
html_table

html_table = html_table.replace('\n', '')
print(html_table)


# In[36]:


#mars hemisphere
mars_url = 'https://marshemispheres.com/'
browser.visit(mars_url)
html=browser.html
soup=bs(html,'html.parser')

hemisphere_image_urls = []

for i in range(4):
    #create empty dictionary
    hemispheres = {}
    browser.find_by_css('a.product-item h3')[i].click()
    element = browser.links.find_by_text('Sample').first
    img_url = element['href']
    title = browser.find_by_css("h2.title").text
    hemispheres["img_url"] = img_url
    hemispheres["title"] = title
    hemisphere_image_urls.append(hemispheres)
    browser.back()
    


# In[37]:


print(hemisphere_image_urls)


# In[38]:


browser.quit()


# In[ ]:




