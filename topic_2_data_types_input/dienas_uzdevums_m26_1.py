# 1. uzdevums
import datetime
 
# Iegūstam pašreizējo gadu
current_year = datetime.datetime.now().year

target_age = 100

# Jautājam lietotāja vārdu
name = input("Kā tevi sauc? ")
 
# Jautājam lietotāja vecumu, izmantojot viņa vārdu
age = int(input(f"Cik tev gadu, {name}? "))
 
# Aprēķinam, pēc cik gadiem būs mērķa vecums
years_to_target = target_age - age
 
# Aprēķina gadu, kad būs mērķa gadi
year_when_target = current_year + years_to_target
 
# Rezultāts
print(f"{name}, pēc {years_to_target} gadiem tev būs {target_age} gadi!")
print(f"Tas būs {year_when_target}. gadā.")