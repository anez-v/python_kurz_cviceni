#Napiš funkci, která bude mít jako vstupní parametr slovo a vrátí slovo, kde zpřehází všechny znaky kromě prvního a posledního.
#Super bonus: Napiš program, který takovou funkci využije na delší text více slov.
#random.shuffle()

text = '''Slovo je stále možné pohodlně přečíst, když jsou pomíchaná písmena.
Stačí, když první a poslední písmeno je na své pozici zachováno. Napiš funkci,
která bude mít jako vstupní parametr slovo a vrátí slovo, kde zpřehází všechny
znaky kromě prvního a posledního.
'''
import random 

def zamichat (slovo):
    k_zamichani = (list(slovo))[1:-1]
    random.shuffle(k_zamichani)
    zamichano = "".join(k_zamichani)
    vysledek = slovo[0] + zamichano + slovo[-1]
    return vysledek

print (zamichat("ahojky"))

#na delsi text
slova = text.split(" ")

novy_text = []
for slovicko in slova: 
    mix = (zamichat(slovicko))
    novy_text.append(mix)
novy_text = " ".join(novy_text)
print(novy_text)