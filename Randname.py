import requests
from bs4 import BeautifulSoup
import random
import unicodedata

#generate random first , last name et date de naissance men fake name generator

baseurl = 'http://www.fakenamegenerator.com/gen-{}-{}-{}.php'

def strip_accents(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')

def gen_emdetails():
    gender = random.choice(['male', 'female'])
    nameset = random.choice(['au', 'us', 'en', 'fr', 'it'])
    country = random.choice(['au', 'as', 'bg', 'ca', 'fr', 'sp'])

    url = baseurl.format(gender, nameset, country)

    url = requests.get(url)
    c = url.content
    bs = BeautifulSoup(c, 'html.parser')
    firstname = strip_accents(bs.find('h3').text.split(" ")[0])
    lastname = strip_accents(bs.find('h3').text.split(" ")[-1])
    mois, jour, annee = bs.find('h3', string='Birthday').next_sibling.next_sibling.find('dd').text.split(' ')
    jour = jour.split(',')[0]
    return firstname, lastname, jour, mois, annee, gender


if __name__ == '__main__':
    gen_emdetails()