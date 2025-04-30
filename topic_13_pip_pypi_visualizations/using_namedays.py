# let's try importing lv-namedays
try:
    import lv_namedays
    print("lv-namedays is installed")
except ImportError:
    print("lv-namedays is not installed. Please install it using 'pip install lv-namedays'")
    exit(1) # nothing to do here`

# let's see what we have in the package
print("lv-namedays package contents:")
print(dir(lv_namedays))

# let's get db object
db = lv_namedays.NameDayDB()
# let's get nameday for May 10th
print(f"Nameday for May 10th: {db.get_names_for_date('05-10')}")

# we could just get whole dictionary
name_dict = db.namedays # so we simply alias it to a shorter name
# let's see first 10 items in the dictionary
print("First 10 items in the dictionary:")
list_items = list(name_dict.items()) # convert to list to get first 10 items
for item in list_items[:10]:
    print(item) # print each item

# let's get today's date in format  'MM-DD' 
# we need to pad month with 0 if it is less than 10
from datetime import datetime
today = datetime.today()
today_str = f"{today.month:02d}-{today.day:02d}"
print(f"Today's date: {today_str}")
# let's get nameday for today
print(f"Nameday for today: {db.get_names_for_date(today_str)}")
