from selenium import webdriver
from random import randint

import urllib

#films on main page
#/html/body/main/div[4]/div[1]/table/tbody/tr/td[1]/div[2]/table/tbody/tr[3]/td/div/div[2]/div[2]/div[1]/a
#/html/body/main/div[4]/div[1]/table/tbody/tr/td[1]/div[2]/table/tbody/tr[3]/td/div/div[{n_film}]/div[2]/div[1]/a
#/html/body/main/div[4]/div[1]/table/tbody/tr/td[1]/div[2]/table/tbody/tr[3]/td/div/div[50]/div[2]/div[1]/a

def post():
    browser = webdriver.Firefox(executable_path=r'C:\\Files\\geckodriver.exe')
    n_page = randint(1,200)
    browser.get(f"https://www.kinopoisk.ru/top/navigator/m_act[num_vote]/100/m_act[rating]/2.5%3A/m_act[tomat_rating]/29%3A/m_act[ex_rating]/3%3A/m_act[is_film]/on/m_act[is_mult]/on/order/rating/page/{n_page}/#results")
    n_film = randint(1,50)
    browser.find_element_by_xpath('/html/body/main/div[4]/div[1]/table/tbody/tr/td[1]/div[2]/table/tbody/tr[3]/td/div/div[50]/div[2]/div[1]/a').click()
    inf_film = {}

    try:
        inf_film['name'] = browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div[2]/div/div[3]/div/div/div[1]/div[1]/div[2]/h1/span').text
    except:
        inf_film['name'] = '_'

    try:
        inf_film['year'] = browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div[2]/div/div[3]/div/div/div[2]/div[1]/div/div[1]/div[2]/a').text
    except:
        inf_film['year'] = '_'

    try:
        inf_film['country'] = browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div[2]/div/div[3]/div/div/div[2]/div[1]/div/div[2]/div[2]/a').text
    except:
        inf_film['country'] = '_'

    try:
        inf_film['duration'] = browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div[2]/div/div[3]/div/div/div[2]/div[1]/div/div[17]/div[2]/div').text.split('/')[0]
    except:
        inf_film['duration'] = '_'

    try:
        inf_film['description'] = browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[3]/div/div/div[1]/div/div[2]/div/div[2]/div/p').text
    except:
        inf_film['description'] = '_'

    img = browser.find_element_by_xpath(f'/html/body/div[2]/div[3]/div[5]/a/img')
    # download the image
    urllib.request.urlretrieve(img.get_attribute('src'), "pic.jpg")
