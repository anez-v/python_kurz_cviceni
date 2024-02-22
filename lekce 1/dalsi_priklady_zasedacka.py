akce = [
    "školení - řízení firemních vozidel",
    "jazykový kurz - angličtina",
    "pohovor - Jan Dvořák",
    "pohovor - Antonín Sova",
    "jazykový kurz - němčina",
    "pohovor - Iveta Hájková",
    "pohovor - Ivan Brož",
    "pohovor - Katarína Martináková",
    "setkání se zákazníkem - Metrostav",
    "jazykový kurz - angličtina",
    "školení - vykazování práce",
    "pohovor - Klaudie Moudrusová",
]


#kolik bylo pohovoru
pocet_pohovoru = 0 
for udalost in akce:
   if "pohovor" in udalost:
      pocet_pohovoru = pocet_pohovoru + 1
print(pocet_pohovoru)

jazyky = []
#jake jazyky se uci
for udalost in akce:
   if "jazykový kurz" in udalost:
      udalost = udalost.split("-")
      jazyk = udalost [1]
      if jazyk not in jazyky:
        jazyky.append(jazyk)

print(jazyky)
