#1
pohyby = [1200, -250, -800, 540, 721, -613, -222]
#Vypište v pořadí třetí pohyb z uvedeného seznamu.
print(pohyby[2])
#Vypište všechny pohyby kromě prvních dvou.
print(pohyby[2:])
#Vypište kolik je všech pohybů dohromady.
print(len(pohyby))
#Pomocí volání vhodných funkcí vypište nejvyšší a nejnižší pohyb.
print(min(pohyby))
print(max(pohyby))
#Spočítejte celkový přírůstek na účtu za dané období. Pozor, že přírůstek může vyjít i záporný.
print(sum(pohyby))

#2
s =  [1200, -250, -800, 540, 721, -613, -222, 333, 150, 254]
v = sum(s)/len(s)
print(v)

#3
rozdil = max(s) - min(s)
print(rozdil)

#bonus1
#najít střed seznamu s (pokud je počet položek sudý, tak ta "prostřední hodnota" blíž ke konci)
stred = s[(len(s)//2)]
print(stred)

#bonus2
#najít střed seznamu s (pokud je počet položek sudý, tak ta "prostřední hodnota" blíž k začátku)
stred = s[(len(s)//2)-1]
print(stred)

