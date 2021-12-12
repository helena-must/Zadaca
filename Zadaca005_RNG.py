#Kreirajte listu imena pomoću recimo ovakvog online name generatora (https://www.behindthename.com/random/). Ispišite jedno po jedno ime, u istoj liniji odvojeno ; znakom.
first_names = ['Pansy', 'Ljiljana', 'Gustav', 'Lauryn', 'Azra']
names_numbers = []

for names in first_names:
    print(f'{names};', end = ' ')

# Pomoću FOR petlje dodajte još 3 imena u listu.
for name in range(3):
    first_names.append(input('Upisi ime: '))
print(first_names)

# Kreirajte novu listu i u nju upišite sva imena iz prethodne liste ali ne kao slova, nego kao brojeve iz ASCII table (https://www.asciitable.com/).
ord_names = []

for name in first_names:
    for letter in name:
        letter = ord(letter)
        ord_names.append(letter)
print(ord_names, end = ' ')       

# Kreirajte program koji će ispisati ASCII tabelu kao na prethodnom linku jedino ne trebate dodavati „html“ stupac.

print('Dec\tHx\tOct\tChar' )
for numbers in range(127 + 1):
    print(numbers,'\t', hex(numbers)[2:],'\t', oct(numbers)[2:],'\t', chr(numbers))



# Kreirajte program koji će za brojeve od 0 do broja kojeg definira korisnik ispisati dekadski, oktalni, heksadekadski, binarni i ASCII znak. Svaki od ovih oblika pohranite u zasebnu listu.

dec_list = []
bin_list = []
hex_list = []
oct_list = []
chr_list = []

for numbers in range(int(input('Upisi broj: '))+1):
    dec_list.append(numbers)
    print(numbers)
    bin_numbers = bin(numbers)
    bin_numbers = bin_numbers[2:]
    bin_list.append(bin_numbers)
    print(bin_numbers)
    hex_numbers = hex(numbers)
    hex_numbers = hex_numbers[2:]
    hex_list.append(hex_numbers)
    print(hex_numbers)
    oct_numbers = oct(numbers)
    oct_numbers = oct_numbers[2:]
    oct_list.append(oct_numbers)
    print(oct_numbers)
    character = chr(numbers)
    chr_list.append(character)
    print(character)

print(dec_list)
print(bin_list)
print(hex_list)
print(oct_list)
print(chr_list)