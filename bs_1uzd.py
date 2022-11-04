# Parašykite programą, kuri nuskaitytų delfi antraštes, patikrintų, 
# ar jos turi dvitaškį. Dalį iki dvitaškio sudėtų į vieną sarašą, 
# dalį po dvitaškio į kitą. Antrą sarašą išmaišykite (google). Tuomet atspausdinkite pirmas dalis iš pirmo sarašo, 
# prie jų prijunkite antras dalis iš antro sąrašo. Turėtume gauti panašių variantų:

# Orai : už 9 šlakius teks sumokėti 26 tūkstančius eurų
# Antradienio vakare kauniečius išgąsdino termofikacijos elektrinė : ar bus naujagimių bumas?
# Sukurkite blogų žodžių sąrašą, pagal kurį išsifiltruoja pranešimai apie COVID, mirtis ir t.t. 
# Išfiltruokite ankstyvoje stadijoje, kol dar antraštės neperskirtos.

import requests
from bs4 import BeautifulSoup
from random import shuffle

html = requests.get('http://delfi.lt').text
soup = BeautifulSoup(html, "html.parser")

title_tags = soup.select('.CBarticleTitle')
titles = [i.get_text() for i in title_tags]
bad_words = ['COVID', 'mirt', 'NVSC', 'skiep']

first_parts = []
second_parts = []
for title in titles:
     if ':' in title:
         if not any(word in title for word in bad_words):
             splitted = title.split(":")
             first_parts.append(splitted[0])
             second_parts.append(splitted[1])

shuffle(second_parts)

for i in range(len(first_parts)):
    print(first_parts[i], ":", second_parts[i])