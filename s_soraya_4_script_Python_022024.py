#!/usr/bin/env python
# coding: utf-8

# In[14]:


# required imports
import pandas as pd
import requests
from PIL import Image


# In[15]:


# see tutorial on how to use the Edamam Food and Grocery Database API with Python : 
# https://rapidapi.com/blog/edamam-food-and-grocery-database-api-with-python-php-ruby-javascript-examples/

# download the data from the API
url = "https://edamam-food-and-grocery-database.p.rapidapi.com/api/food-database/v2/parser"

querystring = {"ingr":"champagne"}

headers = {
    "X-RapidAPI-Key": "722434ac2bmsh98aec1f033708a5p1afa15jsnd51bbdb6176b", # user personal key for the API
    "X-RapidAPI-Host": "edamam-food-and-grocery-database.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)
response = response.json()

response


# In[16]:


# data selection — keeping only the following fields : foodId, label, category, foodContentsLabel, image, 
# for the 10 first products.

data = pd.DataFrame(response['hints'])[:10]

data_dict = {
    "foodId": [],
    "label": [],
    "category" : [],
    "foodContentsLabel" : [],
    "image" : []
}

for i in range(10):
    for key, value in data_dict.items():
        try: data_dict[key].append(data['food'][i][key])
        except: data_dict[key].append(None)

df = pd.DataFrame(data_dict)

df


# In[25]:


# save the data in a .csv file
df.to_csv('first_10_champagne_products.csv')

# download the images and save them
n = 0
for img_url in df['image']:
    try: 
        image_content = requests.get(img_url).content
        with open(f'image{n}.jpg', 'wb') as f:
            f.write(image_content)
    except: 
        pass
    finally: 
        n+=1


# In[26]:


df.info()


# In[27]:


# display an image
Image.open('image0.jpg')

