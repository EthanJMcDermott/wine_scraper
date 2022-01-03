from bs4 import BeautifulSoup
import requests
import time

def find_wine():
    # Last Bottle
    lastbottle = requests.get("https://www.lastbottlewines.com/").text
    soup_lastbottle = BeautifulSoup(lastbottle, 'lxml')
    lastbottle_name = soup_lastbottle.find('h1', class_ = 'offer-name').text
    lastbottle_retail = soup_lastbottle.find('span', class_ = 'amount').text + str(".00")
    lastbottle_price = soup_lastbottle.find('span', class_ = 'amount lb').text + str(".00")
    find_image = soup_lastbottle.find('img')
    lastbottle_image = find_image.attrs['src']
    lastbottle_rating = soup_lastbottle.findAll('span', class_ = 'points-circle')
    for i in range(len(lastbottle_rating)):
        lastbottle_rating[i] = lastbottle_rating[i].text[1:3]
    lastbottle_dict = {
        "title": "Last Bottle",
        "link": "https://www.lastbottlewines.com/",
        "name": lastbottle_name,
        "retail": lastbottle_retail.replace('$','').strip(),
        "price": lastbottle_price.replace('$','').strip(),
        "image": lastbottle_image,
        "ratings": lastbottle_rating
    }


    # Wine Spies
    winespies = requests.get("https://winespies.com/").text
    soup_winespies = BeautifulSoup(winespies, 'lxml')
    winespies_name = soup_winespies.find('span', class_ = 'name').text.replace("  ", '')
    winespies_price = soup_winespies.find('div', class_ = 'amount').text.replace("  ", '')
    winespies_retail = soup_winespies.findAll('div', class_ = 'amount')[1].text.replace(" ", '')
    winespies_image = soup_winespies.find('img', class_ = 'bottle-photo').attrs['data-src'].replace(" ", '')
    winespies_rating = soup_winespies.findAll('span', class_ = 'score')
    winespies_reviewer = soup_winespies.findAll('span', class_ = 'name')
    winespies_rating_award = soup_winespies.find('div', class_ = 'offer-award').find('div', class_ = 'name').text[0:2]
    winespies_reviewer_award = soup_winespies.find('div', class_ = 'offer-award').find('div', class_ = 'category').text
    for i in range(len(winespies_rating)):
        winespies_rating[i] = winespies_rating[i].text
    for i in range(len(winespies_reviewer)):
        winespies_reviewer[i] = winespies_reviewer[i].text
    try:
        int(winespies_rating_award)
        winespies_rating.append(winespies_rating_award)
        winespies_reviewer.append(winespies_reviewer_award)
    except:
        pass
    winespies_dict = {
        "title": "Wine Spies",
        "link": "https://winespies.com/",
        "name": winespies_name,
        "retail": winespies_retail.replace('$','').strip(),
        "price": winespies_price.replace('$','').strip(),
        "image": winespies_image,
        "ratings": winespies_rating,
        "reviwer": winespies_reviewer
    }

    #Cinderella Wine
    cinderella = requests.get("http://cinderellawine.com/").text
    soup_cinderella = BeautifulSoup(cinderella, 'lxml')
    cinderella_name = soup_cinderella.find('div', id = 'title').contents[0].text
    cinderella_price = soup_cinderella.find('p', id = 'product-dollars').text
    cinderella_cents = soup_cinderella.find('p', id = 'product-cents').text
    cinderella_price = cinderella_price + str(".") + cinderella_cents
    cinderella_retail = soup_cinderella.find('p', id = 'reg-price').contents[0].text
    cinderella_image = soup_cinderella.find('div', id = 'bottle-shot').contents[1].attrs['src']
    cinderella_rating = soup_cinderella.find('table').findAll('td')[1].text
    cinderella_reviewer = cinderella_rating.split(" Pts ",1)[1]
    cinderella_rating = [cinderella_rating.split(" Pts ",1)[0]]
    cinderella_dict = {
        "title": "Cinderella Wine",
        "link": "http://cinderellawine.com/",
        "name": cinderella_name,
        "retail": cinderella_retail.replace('$','').strip(),
        "price": cinderella_price.replace('$','').strip(),
        "image": cinderella_image,
        "ratings": cinderella_rating,
        "reviewer": cinderella_reviewer
    }

    #Invino
    invino = requests.get("https://www.invino.com/").text
    soup_invino = BeautifulSoup(invino, 'lxml')
    invino_name = soup_invino.find('h1', class_ = 'product-title').text
    invino_price = soup_invino.find('span', class_ = 'figure-product-actual-price').text
    invino_retail = soup_invino.find('span', class_ = 'figure-product-strikethrough').text
    invino_image = soup_invino.find('img').attrs['src']
    invino_offer_link = soup_invino.find('a', id = 'home-view-offer-link').attrs['href']
    invino_offer = requests.get("https://www.invino.com" + invino_offer_link).text
    soup_invino_offer = BeautifulSoup(invino_offer, 'lxml')
    invino_ratings = soup_invino_offer.findAll('span', class_ = 'review-points')
    invino_reviewers = soup_invino_offer.find('span', class_ = 'review-reviewer').text.split(" - ",1)[0]
    for i in range(len(invino_ratings)):
        invino_ratings[i] = invino_ratings[i].text
    invino_dict = {
        "title": "Invino",
        "link": "https://www.invino.com/",
        "name": invino_name,
        "retail": invino_retail.replace('$','').strip(),
        "price": invino_price.replace('$','').strip(),
        "image": invino_image,
        "ratings": invino_ratings,
        "reviewers": invino_reviewers
    }

    #WTSO
    wtso = requests.get("https://www.wtso.com/").text
    soup_wtso = BeautifulSoup(wtso, 'lxml')
    wtso_name = (soup_wtso.find('h2').text).encode('utf-8')
    wtso_name = wtso_name.replace(b'\xcc', b'')
    wtso_name = wtso_name.replace(b'\x82', b'')
    for i in range(len(wtso_name)-1):
        if wtso_name[i] >= 128:
            wtso_name = wtso_name[0:i] + wtso_name[i+1:]
            i = i-1
    wtso_name = wtso_name.decode('utf-8')
    wtso_image = soup_wtso.find('img', id = 'current-offer-bottle-image').attrs['src']
    wtso_retail = soup_wtso.find('div', id = 'comparable-price').contents[1].text
    wtso_price = soup_wtso.find('span', id = 'price').text
    wtso_ratings_and_reviewers = soup_wtso.findAll('td', class_ = 'show_description')
    wtso_ratings = []
    wtso_reviewers = []
    for i in range(len(wtso_ratings_and_reviewers)//2):
        wtso_ratings.append(wtso_ratings_and_reviewers[i].text.split(" - ",1)[0])
        wtso_reviewers.append(wtso_ratings_and_reviewers[i].text.split(" - ",1)[1])
    wtso_dict = {
        "title": "WTSO",
        "link": "https://www.wtso.com/",
        "name": wtso_name,
        "retail": wtso_retail.replace('$','').strip(),
        "price": wtso_price.replace('$','').strip(),
        "image": wtso_image,
        "ratings": wtso_ratings,
        "reviewers": wtso_reviewers
    }

    #First Bottle
    firstbottle = requests.get("https://www.firstbottlewines.com/").text
    soup_firstbottle = BeautifulSoup(firstbottle, 'lxml')
    firstbottle_name = soup_firstbottle.find('h1').text
    firstbottle_retail = soup_firstbottle.find('span', class_ = 'sale-price').text
    firstbottle_price = soup_firstbottle.find('span', class_ = 'actual-price').text
    firstbottle_image = soup_firstbottle.find('img').attrs['src']
    firstbottle_reviews_link = soup_firstbottle.find('p', class_ = 'details').find('a').attrs['href']
    first_bottle = requests.get("https://www.firstbottlewines.com" + str(firstbottle_reviews_link)).text
    soup_firstbottle_reviews = BeautifulSoup(first_bottle, 'lxml')
    first_bottle_ratings = soup_firstbottle_reviews.findAll('div', class_ = 'review-value')
    first_bottle_reviewers = soup_firstbottle_reviews.findAll('div', class_ = 'review-text')
    firstbottle_reviewers = []
    for i in range(len(first_bottle_reviewers)):
        firstbottle_reviewers.append(first_bottle_reviewers[i].find('p').find('strong').text)
    for i in range(len(first_bottle_ratings)):
        first_bottle_ratings[i] = first_bottle_ratings[i].text
    firstbottle_dict = {
        "title": "First Bottle",
        "link": "https://www.firstbottlewines.com/",
        "name": firstbottle_name,
        "retail": firstbottle_retail.replace('$','').strip(),
        "price": firstbottle_price.replace('$','').strip(),
        "image": firstbottle_image,
        "ratings": first_bottle_ratings,
        "reviewers": firstbottle_reviewers
    }

    #Somm Select
    somm = requests.get("https://www.sommselect.com/daily-offer/").text
    soup_somm = BeautifulSoup(somm, 'lxml')
    somm_name = soup_somm.find('h3').contents[0].text + ' ' + soup_somm.find('h3').contents[1].text
    somm_price = soup_somm.find('a', class_ = 'doffer-add-cart').text
    somm_price = somm_price.split('$',1)[1]
    somm_image = soup_somm.find('div', class_ = 'carousel-item').attrs['style']
    somm_image = somm_image.split('(',1)[1]
    somm_image = somm_image.split(')',1)[0]
    somm_retail = "NA"
    somm_dict = {
        "title": "Somm Select",
        "link": "https://www.sommselect.com/daily-offer/",
        "name": somm_name,
        "retail": somm_retail,
        "price": somm_price.replace('$','').strip(),
        "image": somm_image,
        "ratings": []
    }

    #Parcelle Wine
    parcelle = requests.get("https://parcellewine.com/products/parcelle-pick-todays-deal").text
    soup_parcelle = BeautifulSoup(parcelle, 'lxml')
    parcelle_name = soup_parcelle.find('h1', class_ = 'ProductMeta__Title').text
    parcelle_retail = soup_parcelle.findAll('span', class_ = 'ProductMeta__Price')[0].text
    parcelle_price = soup_parcelle.findAll('span', class_ = 'ProductMeta__Price')[1].text
    parcelle_image = soup_parcelle.find('img', class_ = 'Image--fadeIn').attrs['src']
    parcelle_dict = {
        "title": "Parcelle Wine",
        "link": "https://parcellewine.com/products/parcelle-pick-todays-deal",
        "name": parcelle_name,
        "retail": parcelle_retail.replace('$','').strip(),
        "price": parcelle_price.replace('$','').strip(),
        "image": parcelle_image,
        "ratings": []
    }
    websites = [lastbottle_dict, winespies_dict, cinderella_dict, invino_dict, wtso_dict, firstbottle_dict, somm_dict, parcelle_dict]
    return websites

websites = find_wine()