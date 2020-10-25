#!/usr/bin/env python
# coding: utf-8

# In[5]:


#import libraries
from bs4 import BeautifulSoup
import requests

#reading the instagram URL 
URL="https://www.instagram.com/{}/"
#parse function
def parse_data(s):
    #a dictionary is created
    data={}
    #splitting the content
    #taking first part 
    s=s.split("_")[0]
    #splitting the content again
    s=s.split(" ")
    #assigning the values
    data['Followers'] = s[0]
    data['Following'] = s[2]
    data['Posts'] = s[4]
    #returning the dictionary
    return data

#scraping function
def scrape_data(username):
    #getting the request from URL
    r=requests.get(URL.format(username))
    #converting the text
    s=BeautifulSoup(r.text, "html.parser")
    #finding the meta information
    meta=s.find("meta", property="og:description")
    #calling parse method
    return parse_data(meta.attrs['content'])
#main function for this program
if __name__== "__main__":
    #enter the username you want to dispplay information about
    username ="anu_71199"
    #calling of the scrape function
    data=scrape_data(username)
    #printing statement
    print(data)


# In[ ]:




