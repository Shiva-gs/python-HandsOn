#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Dependencies
import os
from bs4 import BeautifulSoup as bs
from splinter import Browser
import pandas as pd
import time 

def scrape():
    
    # Get the driver and set the executable path
    executable_path = {"executable_path": "/Users/shiva/downloads/chromedriver"}
    browser = Browser("chrome", **executable_path, headless=False)


    # In[7]:

    mars_data={}
    # visit mars url - mission starts
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)


    # In[4]:


    ### NASA Mars News
    print('### NASA Mars News')


    # In[10]:


    # collect the latest News Title and Paragraph Text
    ## Example:
    # news_title = "NASA's Next Mars Mission to Investigate Interior of Red Planet" 
    html=browser.html
    soup = bs(html, 'html.parser')

    latest_news = soup.find("div", class_="list_text")
    news_p = latest_news.find("div", class_="article_teaser_body").text
    news_title = latest_news.find("div", class_="content_title").text
    news_date = latest_news.find("div", class_="list_date").text
    print(news_date)
    print(news_title)
    print(news_p)

    # Add the news date, title and summary to the dictionary
    mars_data["news_date"] = news_date
    mars_data["news_title"] = news_title
    mars_data["summary"] = news_p


    # In[13]:


    print("### JPL Mars Space Images - Featured Image")


    # In[11]:


    # visit the image url
    jpl_url= "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(jpl_url)
    html = browser.html


    # In[12]:


    # Use splinter to navigate the site and find the image url for the current Featured Mars Image
    # Example: featured_image_url = 'https://www.jpl.nasa.gov/spaceimages/images/largesize/PIA16225_hires.jpg'
    # find the image url 
    # right click on the image and inspect get the div name
    soup = bs(html, 'html.parser')
    img_div= soup.find("div", class_="img")
    print(img_div)
    img_div= soup.find("img", class_="thumb")
    print(img_div)

    # get the src
    img_src= soup.find("img", class_="thumb")["src"]
    print(img_src)
    featured_image_url = "https://www.jpl.nasa.gov/"+img_src
    print("***************************")
    print ("featured_image_url "+featured_image_url )
    # get the url for the image
    #img_link = img_div.find("img", class_="thumb").text
    #print(img_link)
    mars_data["featured_image_url"] = featured_image_url


    # In[49]:


    print('### Mars Weather')


    # In[13]:


    # Visit the Mars Weather twitter account 
    # https://twitter.com/marswxreport?lang=en
    twit_url= "https://twitter.com/marswxreport?lang=en"
    browser.visit(twit_url)
    html = browser.html


    # In[14]:


    soup = bs(html, 'html.parser')
    # scrape the latest Mars weather tweet from the page. Save the tweet text
    # Example: mars_weather = 'Sol 1801 (Aug 30, 2017), Sunny, high -21C/-5F, low -80C/-112F, pressure at 8.82 hPa

    weather_div= soup.find("div", class_="js-tweet-text-container")
    print(weather_div.p.text)

    # assign it to variable
    mars_weather = weather_div.p.text
    mars_data["mars_weather"] = mars_weather

    # In[57]:


    print("### Mars Facts")


    # In[15]:


    # Visit the Mars Facts webpage
    fact_url = "https://space-facts.com/mars/"
    browser.visit(fact_url)
    html = browser.html
    soup = bs(html, 'html.parser')


    # In[20]:


    # get the facts 
    fact_header = soup.find("div", class_="widget-header")
    print(fact_header.h3.text)

    fact_data = soup.find("table", class_="tablepress tablepress-id-p-mars")

    # find all rows
    rows = fact_data.find_all('tr')
    fact=[]
    for row in rows:
        print(row.text)
        fact.append(row.text)


    mars_data["mars_table"] = fact


    # In[100]:


    print("### Mars Hemispheres")


    # In[21]:


    # Visit the USGS Astrogeology site 
    #[here](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars)
    astro_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(astro_url)
    html = browser.html
    soup = bs(html, 'html.parser')


    # In[ ]:


    # You will need to click each of the links to the hemispheres 
    # in order to find the image url to the full resolution image

    astro_data = soup.find("div", class_="item")
    astro_link = astro_data.find("div", class_="description")
    print(astro_link.h3)
    #astro_link.h3.click()
    astro_link = browser.find_by_tag('h3')
    len(astro_link)
    mars_hspr =[]

    for i in range(len(astro_link)):
        print(astro_link[i])
        astro_link = browser.find_by_tag('h3')
    
        time.sleep(3)
        astro_link[i].click()
        html = browser.html
    
        soup = bs(html, 'html.parser')
        partial = soup.find("img", class_="wide-image")["src"]
        img_title = soup.find("h2",class_="title").text
    
        img_url = 'https://astrogeology.usgs.gov'+ partial
        dictionary={"title":img_title,"img_url":img_url}
    
        mars_hspr.append(dictionary)
        browser.back()

    mars_data['mars_hemis'] = mars_hspr
    return mars_data


# In[ ]:




