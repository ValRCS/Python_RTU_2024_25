#2.uzdevums - Telpas tilpuma aprēķins
room_lenght = float(input("Telpas garums? "))
room_height = float(input("Telpas augstums? "))
room_width = float(input("Telpas platums?  "))
 
room_volume =  room_lenght * room_height * room_width
 
print(f"Telpas tilpums: {round(room_volume, 3)} m\u00b3")
print(f"Telpas tilpums: {round(room_volume, 3)} m³")
print(f"Telpas tilpums: {room_volume:10.2f} m³")
print(f"Telpas tilpums: {room_volume:3.2f} m³")
# if you only care about how many digits after comma then first part is optional
print(f"Telpas tilpums: {room_volume:.4f} m³")