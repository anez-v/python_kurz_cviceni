#program, který nejprve zkontroluje, zda je host na seznamu, a pokud tam je, zeptá se ho na heslo a zkontroluje jeho správnost. 
#Hostu na seznamu, který zadá správné heslo, vypíše program text: "Smíš vstoupit."

passwords = {"Jiří": "tajne-heslo", "Natálie": "jeste-tajnejsi-heslo", "Klára": "nejtajnejsi-heslo"}
jmeno = input("Zadej jméno:")
vstup = 0
for host in passwords:
    if jmeno == host:
        heslo = input("Zadej heslo:")
        vstup = 1
        if heslo == passwords [host]:
            print("Smíš vstoupit.")
        else:
            print("Sem nelez!")
if vstup == 0:
    print("Sem nelez!")

    

    

