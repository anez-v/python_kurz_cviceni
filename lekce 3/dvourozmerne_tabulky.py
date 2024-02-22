#slovník
book = {"title": "Zkus mě chytit", "sold": 4165, "price": 347, "year": 2018}
#seznam slovníků
books = [
    {"title": "Zkus mě chytit", "sold": 4165, "price": 347, "year": 2018},
    {"title": "Vrah zavolá v deset", "sold": 5681, "price": 299, "year": 2019},
    {"title": "Zločinný steh", "sold": 2565, "price": 369, "year": 2019},
]

#kolik se prodalo celkem knih
total_sales = 0
for item in books:
    total_sales += item["sold"]
print(f"Celkem bylo prodáno {total_sales} knih.")

#za kolik se prodalo
total_sales = 0
for item in books:
    total_sales = total_sales + item["sold"] * item["price"]
print(f"Celkové tržby jsou {total_sales} Kč.")

#kolik se utržilo v roce 2019
total_sales = 0
for item in books:
    if item["year"] == 2019:
        total_sales = total_sales + item["sold"] * item["price"]
print(f"Celkové tržby za knihy prodané v roce 2019 jsou {total_sales} Kč.")


#if "něco" in "něco" funguje jenom na stringy, když chci celé číslo, musím používat <>==
