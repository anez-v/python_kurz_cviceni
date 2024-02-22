#Přečtené knihy - název knihy, počet stran a hodnocení od 0 do 10.
#Napiš program, který spočte celkový počet stran, které Gustav přečetl.
#Připiš do programu výpočet počtu knih, kterým dal Gustav hodnocení alespoň 8.

books = [
    {"title": "Vražda s příliš mnoha notami", "pages": 450, "rating": 5},
    {"title": "Vražda podle knihy", "pages": 524, "rating": 9},
    {"title": "Past", "pages": 390, "rating": 4},
    {"title": "Popel popelu", "pages": 411, "rating": 10},
    {"title": "Noc, která mě zabila", "pages": 159, "rating": 7},
    {"title": "Vražda, kouř a stíny", "pages": 258, "rating": 6},
    {"title": "Zločinný steh", "pages": 542, "rating": 8},
    {"title": "Zkus mě chytit", "pages": 247, "rating": 7},
    {"title": "Vrah zavolá v deset", "pages": 396, "rating": 6},]


#kolik stran celkem 
celkem = 0
for book in books:
    celkem +=(book["pages"])
print(f"Gustav přečetl celkem {celkem} stran!")

#kolik knih s hodnocením 8 a více
lepsi_knihy = 0 
for book in books: 
    if book["rating"] >= 8:
        lepsi_knihy += 1
print(f"Knih co dostalo hodnocení 8 a více: {lepsi_knihy}")




#HORŠÍ ŘEŠENÍ 

#stranky = []
#for item in books:
 #   value = item["pages"]
#    stranky.append(value)
#celkem_stran = sum(stranky)
#print(f"Gustav přečetl celkem {celkem_stran} stran!")



#CIZÍ ŘEŠENÍ
#součet počtu stran
#prectene_stranky = sum(book["pages"] for book in books)
#print("Celkový počet stran přečtených knih:", prectene_stranky)

# součet knih s hodnocením nad 8
#dobre_hodnocene_knizky = sum(1 for book in books if book["rating"] >= 8)
#print("Počet knih s hodnocením alespoň 8:", dobre_hodnocene_knizky)



