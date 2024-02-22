#prumerne teploty
radky =[
    [2001, 7.8],
    [2002, 8.7],
    [2003, 8.2],
    [2004, 7.8],
    [2005, 7.7],
    [2006, 8.2],
    [2007, 9.1],
    [2008, 8.9],
    [2009, 8.4],
    [2010, 7.2]
]

sloupce = [
    [2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010],
    [7.8, 8.7, 8.2, 7.8, 7.7, 8.2, 9.1, 8.9, 8.4, 7.2]
    ]

#1 teplota na třetím řádku 
print(radky[2])
#2 rok na pátém řádku 
print(radky [4][0])
#3 poslední řádek jako seznam
print(radky[-1])
#4 bez pvnich dvou radku
print(radky[2:])
#5 jenom prvni dva
print(radky[:2])
#6 jenom radky 5 až 8
print(radky[4:8])

#7 ze sloupců seřadit vzestupně teplotu
print (sorted (sloupce[1]))