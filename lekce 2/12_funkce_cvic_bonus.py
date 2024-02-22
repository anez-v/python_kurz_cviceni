#text = input("Zadej text:")
#ram = "*" * (len (text) + 4)
#ram2 = "*" * (len (text) + 4)

#print (ram)
#print ("* "+ text + " *")
#print (ram2) 

def ramecek (znak, text):
    radek = znak * (len (text) + 4)
    radek2 = (znak + " " + text + " " + znak)
    print(radek + "\n" + radek2 + "\n" + radek)
    #print("\n".join([radek, radek2, radek]))

ramecek("*", "ahoj")

#Funkce ze zadaného rodného čísla určí měsíc narození, které vrátí jako výstup
#Nezapomeň, že pro ženy je k měsíci připočtena hodnota 50.
#Příklad: Pro hodnotu 9207054439 vrátí 7. Pro hodnotu 9555125899 vrátí 5

def month_of_birth (rodne_cislo):
    rodne_cislo = str(rodne_cislo)
    mesic = int(rodne_cislo [2:4])
    if mesic >= 50:
        print(mesic - 50)
    else:
        print(mesic)

month_of_birth(9207054439)
month_of_birth(9555125899)
