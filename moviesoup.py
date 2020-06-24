# !/bin/python3
#enter movie name, prints output of critic score

#imports

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

def urlify(s):
    #replace whitepsace with underscore for urls
    s = re.sub(r"\s+", '_', s)

    return s
#input for movie
movie_title = input("which movie?\n")
movie_title = urlify(movie_title)


sub_site = 'https://www.rottentomatoes.com/m/'
site = urlopen(sub_site + movie_title)
#site = urlopen("https://www.rottentomatoes.com/m/the_lord_of_the_rings_the_fellowship_of_the_ring")
movie = BeautifulSoup(site.read(), features="lxml")
for rating in movie.find_all('span', class_='mop-ratings-wrap__percentage'):
    print(rating.get_text())

