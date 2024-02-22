#1
cislo = 100
print(cislo)
cislo = cislo + 1
print(cislo)  # Vypíše 101

#2
# Ulož do proměnné cislo vstup od uživatele

cislo = int(input("Zadej číslo."))
print(cislo)  # Zopakuje zadanou hodnotu
cislo = cislo + 1
print(cislo)  # Vypíše cislo zvětšené o 1

#3
#převod Fahrenheit na Celsius
teplota_F = float(input("Zadej teplotu ve stupních Fahrenheita."))
teplota_C = float(5 * (teplota_F - 32))/9
print(f"Teplota ve stupních Celsia je {teplota_C}")