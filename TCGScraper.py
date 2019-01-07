from bs4 import BeautifulSoup
import time
import json
import requests
from time import sleep
import re


#url = "https://www.pokemon.com/us/pokemon-tcg/pokemon-cards/sm-series/sm8/52/"
#url = "https://www.pokemon.com/us/pokemon-tcg/pokemon-cards/sm-series/sm8/178/" #Example of stadium card
url = "https://www.pokemon.com/us/pokemon-tcg/pokemon-cards/bw-series/bw7/20/"

start = time.time()
r = requests.get(url)
r_unparsed = r.text

b = BeautifulSoup(r_unparsed,'lxml')


card  = b.find('h1').text
print(card)

cardType = b.find('h2').text.strip()

if("Trainer" in cardType):
    cardType = re.split(' -|, |\*|\n|\[(.*?)\]| ',cardType)
    cardType = list(filter(None, cardType))
    print("This is a Trainer Card: {0}".format(cardType[1]))
else:
    print("This is a Pokemon: {0}".format(cardType))


abilities = b.find_all('div','ability')
print("Moves: ")
for ability in abilities:
    move_cost=[]
    # try:
    for moveName in ability.find_all('h4'):
        print(moveName.text.strip())

    for moveCost in ability.find_all('span'):
        print("{0} Damage".format(moveCost.text.strip()))
    try:
        print(ability.find('pre').text.strip())
    except Exception as e:
        print(ability.find('p').text.strip())

    for cost in ability.find_all('li'):
        move_cost.append(cost.get('title', 'No title attribute'))

    print(move_cost)
    print("")


end = time.time()
print("Elapsed time: {0}".format(end - start))
