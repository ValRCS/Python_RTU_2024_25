#3. uzdevums
celsium = float(input("Ievadi temperatūru celsijos:"))
fahrenheit = 32+(celsium*(9/5))
print(f"Temperatūra fārenheitā: {fahrenheit}")
print(f"Temperatūra fārenheitā: {fahrenheit:.4f}")
# alternative is to round the data to some precision
fahrenheit_rounded = round(fahrenheit, 2)
print(f"Temperatūra fārenheitā lidz 2 cipariem aiz kom: {fahrenheit_rounded}")
