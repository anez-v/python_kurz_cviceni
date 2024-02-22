#1
jmeno = "Anežka Votrubová"
jmeno = jmeno.upper ()
print(jmeno)

jmeno = "Anežka Votrubová"
jmeno = jmeno.lower ()
print(jmeno)

#2 
#přičíst 4 k 7 (na druhé/třetí pozici) a pak to vyjet zas jako list stringů
hodnoty = ['12', '1', '7', '-11']
vysledek = int(hodnoty[2]) + 4
hodnoty[2] = str(vysledek)
print(hodnoty)

#3
#split ze string udělá list 
hodnoty = '12.1 1.68 7.45 -11.51'
seznam_cisel = hodnoty.split(" ")
x = seznam_cisel [-1]
vysledek2 = float(x) + 0.25
seznam_cisel[-1] = str(vysledek2)
seznam_cisel = " ".join(seznam_cisel)
print(seznam_cisel)


#4
#zjednodušit cvič. 2 až na jeden řádek
hodnoty = ['12', '1', '7', '-11']
hodnoty[2] = str(int(hodnoty[2]) + 4)
print(hodnoty)

hodnoty = ['12', '1', '7', '-11']
print(hodnoty[0:2] + [(str(int(hodnoty[2]) + 4))] + hodnoty [-1:])


