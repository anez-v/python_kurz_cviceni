import requests
import sys


#hledani podle ičo
ico = input("Zadejte IČO:")
adresa = f"https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/{ico}"
response = requests.get(url=adresa)
data = response.json()

if response.status_code != 200:
    print("IČO nebylo nalezeno nebo server neodpovídá.")
    sys.exit()

obchodni_jmeno = data["obchodniJmeno"]
adresa_sidla = data["sidlo"]["textovaAdresa"]

print(obchodni_jmeno,"\n", adresa_sidla)


#hledani podle jmena nebo jeho casti
#bonus - pravni forma

headers = {
    "accept": "application/json",
    "Content-Type": "application/json",
}

data = '{"kodCiselniku": "PravniForma", "zdrojCiselniku": "res"}'
res = requests.post("https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ciselniky-nazevniky/vyhledat", headers=headers, data=data)
odpoved = res.json()
polozky_ciselniku = odpoved["ciselniky"][0]["polozkyCiselniku"]


def find_legal_form(kod, polozky_ciselniku):
    kod = kod
    for polozka in polozky_ciselniku:
        kod_nazvu = polozka["kod"]
        nazev = polozka["nazev"][0]["nazev"]
        if kod == kod_nazvu:
            return nazev
    raise ValueError("Neplatný kód")


headers = {
    "accept": "application/json",
    "Content-Type": "application/json",
}
jmeno = input("Zadejte jméno nebo jeho část:")

data = {"obchodniJmeno": jmeno}
res = requests.post("https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/vyhledat", headers=headers, json=data)
odpoved_a = res.json()
print(odpoved_a)

pocet_celkem = odpoved_a["pocetCelkem"]
print(f"Nalezeno subjektů: {pocet_celkem}")


ekon_subjekty = odpoved_a["ekonomickeSubjekty"]
for subjekt in ekon_subjekty:
    kod = subjekt['pravniForma']
    pravni_forma = find_legal_form(kod, polozky_ciselniku)
    print(f"{subjekt['obchodniJmeno']}, {subjekt['ico']}, {pravni_forma}")


