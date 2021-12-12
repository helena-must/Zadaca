# chr range od 32 do 73

for broj in range(32,73):
    print(chr(broj), end=' ',) 
    # Mogu li ovdje nekako napraviti da zadnji end bude novi red? 
    # Dakle samo razmak izmedu elemenata, ali na kraju novi red.
    
print()
print()
recenica = 'Ovo je test recenica'

# ord slova u recenici

for slovo in recenica:
    print(ord(slovo), end= ' ')
print()

# uzeti listu imena, ispisati sva imena i jos jedan for loop za svako slovo u imenu

lista_imena = ['Petar Peric', 'Ivan Ivanovic', 'Martin Martinovic']

for imena in lista_imena:
    for slovo in imena:
        print(slovo, end = ' ')

bin_lista = []
hex_lista = []

# uzeti dekadsku listu do 100, pretvoriti u bin i hex i izbaciti prvi dio

for broj in range(101):
    bin_broj = bin(broj)
    bin_broj = bin_broj[2:]
    bin_lista.append(bin_broj)
    hex_broj = hex(broj)
    hex_broj = hex_broj[2:]
    hex_lista.append(hex_broj)
print(bin_lista)
print(hex_lista)

'''
Kreirajte listu imena pomoću recimo ovakvog online name generatora (https://www.behindthename.com/random/). Ispišite jedno po jedno ime, u istoj liniji odvojeno ; znakom.
Pomoću FOR petlje dodajte još 3 imena u listu.
Kreirajte novu listu i u nju upišite sva imena iz prethodne liste ali ne kao slova, nego kao brojeve iz ASCII table (https://www.asciitable.com/).
Kreirajte program koji će ispisati ASCII tabelu kao na prethodnom linku jedino ne trebate dodavati „html“ stupac.
Kreirajte program koji će za brojeve od 0 do broja kojeg definira korisnik ispisati dekadski, oktalni, heksadekadski, binarni i ASCII znak. Svaki od ovih oblika pohranite u zasebnu listu.
 
'''

