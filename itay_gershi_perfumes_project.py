#!/usr/bin/env python
# coding: utf-8

# ##  ?איך ניתן לחזות איזה בשמים הולכים להיות המובילים השנה 
# 
# 
# ##  how can you predict which perfumes are going to be top this year?
# 

# # הגדרות:

# In[390]:


import bs4
from splinter import Browser
from bs4 import BeautifulSoup
import time
from webdriver_manager.chrome import ChromeDriverManager
import requests
import pandas as pd
import re
import selenium
from pandas import DataFrame
import json
from selenium import webdriver
import scipy as sc
import numpy as np
import time
import os
import requests

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
print("1")


# In[419]:


driver = webdriver.Chrome()

link_hrefs=list()
for i in range(1,100):
    
    driver.get('https://www.fragrancex.com/shopping/best?instock=false&currentPage=' + str(i) + '&searchSortExpression=0')
    driver.implicitly_wait(10)
    more_items_elements = driver.find_elements(By.CLASS_NAME,'search-result-grid')

    for more_items_element in more_items_elements:
        link_elements = more_items_element.find_elements(By.CSS_SELECTOR, 'a.link-2')
        for link_element in link_elements:
            link_hrefs.append(link_element.get_attribute('href'))

len(link_hrefs)


# In[420]:


driver.close()


# In[426]:


####### CREATING ALL LIST'S #######
brand_name_LIST=[]
fragrance_family_LIST=[]
fragrance_name_LIST=[]
fragrance_classification_LIST=[]
volume_LIST=[]
top_notes_LIST=[]
heart_notes_LIST=[]
base_notes_LIST=[]
gender_LIST=[]
ingredients_LIST=[]
product_form_LIST=[]
year_of_launch_LIST = []
strength_LIST = []
sustainable_LIST = []
country_of_origin_LIST = []

reviews_LIST = []
grade_LIST = []

grade_5_stars_LIST = []
grade_4_stars_LIST = []
grade_3_stars_LIST = []
grade_2_stars_LIST = []
grade_1_stars_LIST = []

respondants_would_recommend_this_to_a_friend_LIST = []

col_name = {'name','company','sex','Perfumer','Component','rating','rating count'}


# In[435]:


from selenium.common.exceptions import NoSuchElementException
sum_perfume_succeeded=0
driver2 = webdriver.Chrome()

for i in link_hrefs:
    driver2.get(i)
        
    # Find all tr elements on the page
    table = driver2.find_element(By.TAG_NAME,'tbody')
    elements = table.find_elements(By.TAG_NAME,'tr')
    
    # Create empty lists to store the text from each td element
    name_elements = []
    text_elements = []

    # Iterate through the tr elements and extract the text from each td element
    for element in elements:
        tds = element.find_elements(By.TAG_NAME, 'td')
        name_elements.append(tds[0].text)
        text_elements.append(tds[1].text)
    
    #This code will check if the string "...." is in the name_elements list and if yes insert to ""...."_name_LIST else NAN
    try:
        index = name_elements.index("Brand")
        brand_name_LIST.append(text_elements[index])
    except NoSuchElementException:
        brand_name_LIST.append(None)
        
    try:
        index = name_elements.index("Fragrance Family")
        fragrance_family_LIST.append(text_elements[index])
    except NoSuchElementException:
        fragrance_family_LIST.append(None)
        
    
    try:
        index = name_elements.index("Fragrance Name")
        fragrance_name_LIST.append(text_elements[index])
    except NoSuchElementException:
        fragrance_name_LIST.append(None)

    try:
        index = name_elements.index("Fragrance Classification")
        fragrance_classification_LIST.append(text_elements[index])
    except NoSuchElementException:
        fragrance_classification_LIST.append(None)
       
    try:
        index = name_elements.index("Volume")
        volume_LIST.append(text_elements[index])
    except NoSuchElementException:
        volume_LIST.append(None)

    
    
    try:
        index = name_elements.index("Top Notes")
        top_notes_LIST.append(text_elements[index])
    except NoSuchElementException:
        top_notes_LIST.append(None)
    
    
    try:
        index = name_elements.index("Heart Notes")
        heart_notes_LIST.append(text_elements[index])
    except NoSuchElementException:
        heart_notes_LIST.append(None)

        
    try:
        index = name_elements.index("Base Notes")
        base_notes_LIST.append(text_elements[index])
    except NoSuchElementException:
        base_notes_LIST.append(None)
        
        
    try:
        index = name_elements.index("Gender")
        gender_LIST.append(text_elements[index])
    except NoSuchElementException:
        gender_LIST.append(None)
    

    try:
        index = name_elements.index("Product Form")
        product_form_LIST.append(text_elements[index])
    except NoSuchElementException:
        product_form_LIST.append(None)

        
    try:
        index = name_elements.index("Year Of Launch")
        year_of_launch_LIST.append(text_elements[index])
    except NoSuchElementException:
        year_of_launch_LIST.append(None)

        
        
    try:
        index = name_elements.index("Strength")
        strength_LIST.append(text_elements[index])
    except NoSuchElementException:
        strength_LIST.append(None)
 
    try:
        index = name_elements.index("Sustainable")
        sustainable_LIST.append(text_elements[index])
    except NoSuchElementException:
        sustainable_LIST.append(None)

          
    try:
        index = name_elements.index("Country of Origin")
        country_of_origin_LIST.append(text_elements[index])
    except NoSuchElementException:
        country_of_origin_LIST.append(None)
        
        
    try:
        index = name_elements.index("Ingredients")
        ingredients_LIST.append(text_elements[index])
    except NoSuchElementException:
        ingredients_LIST.append(None)
       
        
    try:
        rating_element = driver2.find_element(By.CSS_SELECTOR, 'div[itemprop="ratingValue"][class="h2 serif header-large"]')
        grade_LIST.append(rating_element.text)
    except NoSuchElementException:
        grade_LIST.append(None)
 
    try:
        review_count_element = driver2.find_element(By.CSS_SELECTOR, 'div[itemprop="reviewCount"][class="review-count"]')
        review_count = review_count_element.get_attribute('content')
        reviews_LIST.append(review_count)
    except NoSuchElementException:
        reviews_LIST.append(None)

        
    #sum_perfume_succeeded = sum_perfume_succeeded+1
    #if(sum_perfume_succeeded==100):
    #    driver2.quit()
driver2.quit()
print(sum_perfume_succeeded)


# In[428]:


print(len(strength_LIST))


# In[ ]:


#tds = elements[9].find_elements(By.TAG_NAME, 'td')
#ingredients_LIST.append(tds[1].text)
   
#reviews_LIST.append
#grade_LIST.append

#grade_5_stars_LIST.append
#grade_4_stars_LIST.append
#grade_3_stars_LIST.append
#grade_2_stars_LIST.append
#grade_1_stars_LIST.append


# In[429]:


df = pd.DataFrame({'Brand':brand_name_LIST,'grade':grade_LIST,'reviews':reviews_LIST,'fragrance family':fragrance_family_LIST,'fragrance name':fragrance_name_LIST,
                   'fragrance classification':brand_name_LIST,'volume':volume_LIST,'top notes':top_notes_LIST,
                  'heart notes':heart_notes_LIST,'base notes':base_notes_LIST,'gender':gender_LIST,
                  'product form':product_form_LIST,'year of launch':year_of_launch_LIST,'strength':strength_LIST,
                  'sustainable':sustainable_LIST,'country of origin':country_of_origin_LIST,'ingredients':ingredients_LIST})
df


# In[277]:





# In[279]:


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": ChromeDriverManager().install()}
    return Browser("chrome", **executable_path, headless=False)


# In[280]:


browser = init_browser()
url = "https://www.fragrantica.com/search/"
browser.visit(url)


# In[281]:


# Start over whenever you change years or after error troubleshooting 
html = browser.html
soup = bs(html, "html.parser")


# In[282]:


for i in range(2019,2020):
    
    browser.find_by_css('input[type="number"]')[1].fill(i)
    browser.find_by_css('input[type="number"]')[0].fill(i)
    time.sleep(5)
 

    for j in range(0,100):
                try:
                    browser.find_by_css('button[class="button"]').click()
                except:
                    break
    
    html = browser.html
    soup = bs(html, "html.parser")
    
    ####### GET THE LENGTH OF THE RESULTS #######
    block1 = soup.find("span", class_="grid-x grid-margin-x grid-margin-y small-up-3 medium-up-2 large-up-4 perfumes-row text-center")
    perfume_name_list = []
    
    for perf_text in block1.find_all("a", href=True):
        perf_name = perf_text.get_text()
        perfume_name_list.append(perf_name.replace('\n', '').strip(" "))
        
    ####### START ITERATING THROUGH THE PERFUMES OF THAT YEAR ####### 
    for k in range(len(perfume_name_list)):
        
        html = browser.html
        soup = bs(html, "html.parser")
            
        browser.find_by_css('span[class="link-span"]')[k].click()

        time.sleep(5)

        html = browser.html
        soup = bs(html, "html.parser")

        time.sleep(5)
            
        perfume_name = soup.find_all("div", class_="cell small-12")[3].find_all("b")[0].get_text()
        perfume_comp = soup.find_all("div", class_="cell small-12")[3].find_all("b")[1].get_text()

        perfume_image = soup.find_all("div", class_="cell small-12")[1].find("img")["src"]

        for_gender = soup.find("small").get_text()
            
        try:
            rating = float(soup.find("p", class_="info-note").find_all("span")[0].get_text())
            number_votes = int(soup.find("p", class_="info-note").find_all("span")[2].get_text().replace(',', ''))
        except:
            rating = "NA"
            number_votes = "NA"
            print(f"{perfume_name} does not have a ranking")
        
        ####### MAIN ACCORDS DICTIONARY #######
        try:
            description = soup.find_all("div", class_="cell small-12")[3].get_text()
        except:
            description = "NA"
            print(f"{perfume_name} does not have a description")
            
        try:
            main_accords = soup.find_all("div", class_="cell accord-box")
            accords_dict = {}
            for m in range(len(main_accords)):
                accord_name = main_accords[m].get_text()
                accord_value = float(main_accords[m].find("div", class_="accord-bar")["style"].rsplit("width: ")[1].strip("%;"))
                accords_dict[accord_name] = accord_value
        except:
            accords_dict = {}
            print(f"{perfume_name} does not have accords")
                
        ####### FRAGRANCE NOTES #######            
        notes = soup.find_all("div", attrs={"style": "display: flex; justify-content: center; text-align: center; flex-flow: row wrap; align-items: flex-end; padding: 0.5rem;"})

        if len(notes) == 3:
            number = 2
            top_notes_list = []
            middle_notes_list = []
            base_notes_list = []

            for n in range(len(notes[0].find_all("span", class_="link-span"))):
                top_notes_list.append(notes[0].find_all("div")[number].get_text())
                number += 3

            number = 2
            for p in range(len(notes[1].find_all("span", class_="link-span"))):
                middle_notes_list.append(notes[1].find_all("div")[number].get_text())
                number += 3

            number = 2
            for q in range(len(notes[2].find_all("span", class_="link-span"))):
                base_notes_list.append(notes[2].find_all("div")[number].get_text())
                number += 3
        elif len(notes) == 2:
            number = 2
            top_notes_list = []
            middle_notes_list = []
            base_notes_list = []

            for r in range(len(notes[0].find_all("span", class_="link-span"))):
                top_notes_list.append(notes[0].find_all("div")[number].get_text())
                number += 3

            number = 2
            for s in range(len(notes[1].find_all("span", class_="link-span"))):
                middle_notes_list.append(notes[1].find_all("div")[number].get_text())
                number += 3
        elif len(notes) == 1:
                
            number = 2
            top_notes_list = []
            middle_notes_list = []
            base_notes_list = []

            for v in range(len(notes[0].find_all("span", class_="link-span"))):
                middle_notes_list.append(notes[0].find_all("div")[number].get_text())
                number += 3
        else:
            top_notes_list = []
            middle_notes_list = []
            base_notes_list = []

        ####### VOTING DATA & INFORMATION #######
        voting = soup.find_all("div", class_="cell small-1 medium-1 large-1")

        ####### Longevity #######
        long_v_weak = int(voting[0].get_text())
        long_weak = int(voting[1].get_text())
        long_moderate = int(voting[2].get_text())
        long_long_last = int(voting[3].get_text())
        long_eternal = int(voting[4].get_text())

        ####### Sillage #######
        sill_intimate = int(voting[5].get_text())
        sill_moderate = int(voting[6].get_text())
        sill_strong = int(voting[7].get_text())
        sill_enormus = int(voting[8].get_text())

        ####### Gender #######
        gender_female = int(voting[9].get_text())
        gender_more_fem = int(voting[10].get_text())
        gender_unisex = int(voting[11].get_text())
        gender_more_male = int(voting[12].get_text())
        gender_male = int(voting[13].get_text())
            
            
        ####### Price Value #######
        value_w_over = int(voting[14].get_text())
        value_over = int(voting[15].get_text())
        value_ok = int(voting[16].get_text())
        value_good = int(voting[17].get_text())
        value_great = int(voting[18].get_text())
        
        
        ####### CREATING THE DICTIONARY OF DATA #######
        perfume_dict = {"name": perfume_name,
                        "company": perfume_comp,
                        "image": perfume_image,
                        "for_gender": for_gender,
                        "rating": rating,
                        "number_votes": number_votes,
                        "main accords": accords_dict,
                        "description": description,
                        "top notes": top_notes_list,
                        "middle notes": middle_notes_list,
                        "base notes": base_notes_list,
                        "longevity":   {"very weak": long_v_weak,
                                        "weak": long_weak,
                                        "moderate": long_moderate,
                                        "long lasting": long_long_last,
                                        "eternal": long_eternal},
                        "sillage":     {"intimate": sill_intimate,
                                        "moderate": sill_moderate,
                                        "strong": sill_strong,
                                        "enormous": sill_enormus},
                        "gender_vote": {"female": gender_female,
                                        "more female": gender_more_fem,
                                        "unisex": gender_unisex,
                                        "more male": gender_more_male,
                                        "male": gender_male},
                        "price value": {"way overpriced": value_w_over,
                                        "overpriced": value_over,
                                        "ok": value_ok,
                                        "good value": value_good,
                                        "great value": value_great}
                           }
        list_of_perfume_dicts.append(perfume_dict)

        time.sleep(2)

        browser.back()
            
        time.sleep(2)
        
            

            


# In[ ]:


#perfume_name_list
#data_fram = pd.DataFrame(perfume_name_list)
len(perfume_name_LIST)


# In[ ]:


len(list_of_perfume_dicts)


# In[138]:


with open ("perfume_data_2017_plus.json", "w") as f:
    json.dump(list_of_perfume_dicts, f)


# In[ ]:


####################################################
####### USE THIS FOR A SINGULAR PERFUME PAGE #######
############### NOT THE SEARCH PAGE ###############
###################################################


html = browser.html
soup = bs(html, "html.parser")

time.sleep(1)

####### PULL FROM ORIGINAL NAME LIST #######
perfume_name = soup.find_all("div", class_="cell small-12")[3].find_all("b")[0].get_text()
perfume_comp = soup.find_all("div", class_="cell small-12")[3].find_all("b")[1].get_text()

perfume_image = soup.find_all("div", class_="cell small-12")[1].find("img")["src"]

for_gender = soup.find("small").get_text()

try:
    rating = float(soup.find("p", class_="info-note").find_all("span")[0].get_text())
    number_votes = int(soup.find("p", class_="info-note").find_all("span")[2].get_text().replace(',', ''))
except:
    rating = "NA"
    number_votes = "NA"
    print(f"{perfume_name} does not have a ranking")

try:
    description = soup.find_all("div", class_="cell small-12")[3].get_text()
except:
    description = "NA"
    print(f"{perfume_name} does not have a description")

####### MAIN ACCORDS DICTIONARY #######

try:
    main_accords = soup.find_all("div", class_="cell accord-box")
    accords_dict = {}
    for m in range(len(main_accords)):
        accord_name = main_accords[m].get_text()
        accord_value = float(main_accords[m].find("div", class_="accord-bar")["style"].rsplit("width: ")[1].strip("%;"))
        accords_dict[accord_name] = accord_value
except:
    accords_dict = {}
    print(f"{perfume_name} does not have accords")

####### FRAGRANCE NOTES #######        
notes = soup.find_all("div", attrs={"style": "display: flex; justify-content: center; text-align: center; flex-flow: row wrap; align-items: flex-end; padding: 0.5rem;"})

if len(notes) == 3:
    number = 2
    top_notes_list = []
    middle_notes_list = []
    base_notes_list = []

    for n in range(len(notes[0].find_all("span", class_="link-span"))):
        top_notes_list.append(notes[0].find_all("div")[number].get_text())
        number += 3

    number = 2
    for p in range(len(notes[1].find_all("span", class_="link-span"))):
        middle_notes_list.append(notes[1].find_all("div")[number].get_text())
        number += 3

    number = 2
    for q in range(len(notes[2].find_all("span", class_="link-span"))):
        base_notes_list.append(notes[2].find_all("div")[number].get_text())
        number += 3
elif len(notes) == 2:
    number = 2
    top_notes_list = []
    middle_notes_list = []
    base_notes_list = []

    for r in range(len(notes[0].find_all("span", class_="link-span"))):
        top_notes_list.append(notes[0].find_all("div")[number].get_text())
        number += 3

    number = 2
    for s in range(len(notes[1].find_all("span", class_="link-span"))):
        middle_notes_list.append(notes[1].find_all("div")[number].get_text())
        number += 3
elif len(notes) == 1:
    number = 2
    top_notes_list = []
    middle_notes_list = []
    base_notes_list = []

    for v in range(len(notes[0].find_all("span", class_="link-span"))):
        middle_notes_list.append(notes[0].find_all("div")[number].get_text())
        number += 3
else:
    top_notes_list = []
    middle_notes_list = []
    base_notes_list = []

####### VOTING DATA & INFORMATION #######
voting = soup.find_all("div", class_="cell small-1 medium-1 large-1")

####### Longevity #######
long_v_weak = int(voting[0].get_text())
long_weak = int(voting[1].get_text())
long_moderate = int(voting[2].get_text())
long_long_last = int(voting[3].get_text())
long_eternal = int(voting[4].get_text())

####### Sillage #######
sill_intimate = int(voting[5].get_text())
sill_moderate = int(voting[6].get_text())
sill_strong = int(voting[7].get_text())
sill_enormus = int(voting[8].get_text())

####### Gender #######
gender_female = int(voting[9].get_text())
gender_more_fem = int(voting[10].get_text())
gender_unisex = int(voting[11].get_text())
gender_more_male = int(voting[12].get_text())
gender_male = int(voting[13].get_text())

####### Price Value #######
value_w_over = int(voting[14].get_text())
value_over = int(voting[15].get_text())
value_ok = int(voting[16].get_text())
value_good = int(voting[17].get_text())
value_great = int(voting[18].get_text())

####### CREATING THE DICTIONARY OF DATA #######
perfume_dict = {"name": perfume_name,
                "company": perfume_comp,
                "image": perfume_image,
                "for_gender": for_gender,
                "rating": rating,
                "number_votes": number_votes,
                "main accords": accords_dict,
                "description": description,
                "top notes": top_notes_list,
                "middle notes": middle_notes_list,
                "base notes": base_notes_list,
                "longevity":   {"very weak": long_v_weak,
                                "weak": long_weak,
                                "moderate": long_moderate,
                                "long lasting": long_long_last,
                                "eternal": long_eternal},
                "sillage":     {"intimate": sill_intimate,
                                "moderate": sill_moderate,
                                "strong": sill_strong,
                                "enormous": sill_enormus},
                "gender_vote": {"female": gender_female,
                                "more female": gender_more_fem,
                                "unisex": gender_unisex,
                                "more male": gender_more_male,
                                "male": gender_male},
                "price value": {"way overpriced": value_w_over,
                                "overpriced": value_over,
                                "ok": value_ok,
                                "good value": value_good,
                                "great value": value_great}
               }
list_of_perfume_dicts.append(perfume_dict)

time.sleep(2)

browser.back()
 


# In[173]:


list_of_perfume_dicts

