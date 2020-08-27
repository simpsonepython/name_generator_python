import requestes as requestes
import requests
from random import randint

print("Witam w generatorze imion !\n Proszę napisz swoję prawdziwe imie a wygenerujemy ci losowe")
a = input("Podaj swoję prawdziwe imię tutaj: ")


url = "https://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
r = requests.get(url)
text = r.text
##print(text)

jedno_imie = text.split()

#print(jedno_imie)

random_imie = randint(0,len(jedno_imie))

print("Wylosowaliśmy dla ciebie drugie imię o to one:", jedno_imie[random_imie] )



