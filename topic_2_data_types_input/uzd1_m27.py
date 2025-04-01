# 1. Uzdevums
name = input("Labdien! Kā Jūs sauc?")
age = int(input(f"Cik jums ir gadi {name}?"))
import datetime
current_year = datetime.datetime.now().year
target_age = 100
years_to_target = target_age - age
year_target_reached = current_year + years_to_target
print(f"{target_age} gadi Jums būs {year_target_reached} gadā, proti pēc {years_to_target} gadiem.")
print("*"*50)