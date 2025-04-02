#2.uzdevums
# 2.Uzdevums
star_count = 40
min_years = 2
bonus_rate = 0.15

salary = float(input("Kāda Jums ir mēneša alga?  "))
years_worked = int(float(input("Cik pilnus gadus Jūs nostrādājāt uzņēmumā?  ")))
if years_worked > min_years:
    bonus = (years_worked - min_years) * salary * bonus_rate
    print(f"Jūsu Ziemassvētku bonuss būs {bonus:.2f} EUR.")
else:
    print("Diemžēl, Jums šogad Ziemassvētku bonuss nepienākās 😞 ")

print("*"*star_count)