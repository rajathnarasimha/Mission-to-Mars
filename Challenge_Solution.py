#!/usr/bin/env python
# coding: utf-8

# In[1]:


from splinter import Browser
from bs4 import BeautifulSoup
import urllib.request


# In[2]:


# Path to chromedriver
get_ipython().system('which chromedriver')


# In[7]:


# Mac users
executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)


# In[8]:


url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)

# Parse the HTML
html = browser.html
soup = BeautifulSoup(html, 'html.parser')


# In[9]:


#Challenge Solution

url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)

# Parse the HTML
html = browser.html
soup = BeautifulSoup(html, 'html.parser')

section = soup.find('div', class_='collapsible results')
items = section.find_all('div', class_='description')

urls=[]
titles=[]

for item in items:
    src = item.find_all('a')
    for i in src:
        urls.append(i.get('href'))
        
    title = item.find_all('h3')
    for i in title:
        titles.append(i.text)

print(f"The titles of the mars hemispehers are: \n{titles}\n")

img_urls=[]
for url in urls:
    img_urls.append('https://astrogeology.usgs.gov'+url)

print(f"The hemispheres links to get the full images: \n{img_urls}\n")

full_img_urls=[]
for img_url in img_urls:
    html_page = urllib.request.urlopen(img_url)
    soup = BeautifulSoup(html_page, "html.parser")
    section = soup.find('img', class_='wide-image')
    img=section['src']
    full_img_urls.append('https://astrogeology.usgs.gov' + img)
    
print(f"\n The links for the hemispheres full images: \n{full_img_urls}\n")

mars_hemisphere_dict={}
for key in titles:
    for value in full_img_urls:
        mars_hemisphere_dict[key] = value
        full_img_urls.remove(value)
        break
print(f"The mars hemisphere names with image links: \n{mars_hemisphere_dict}\n")


mars_hemisphere_list=[]
for key, value in mars_hemisphere_dict.items():
    mars_hemisphere_list.append((key, value))
    
print(f"The list of hemisphere and its details: \n{mars_hemisphere_list}\n")


# In[ ]:




