
from datetime import datetime, timedelta
from collections import defaultdict

users = [
    {"name": "Anatolii", "birthday": datetime (1990, 4, 12)},
    {"name": "Elena", "birthday": datetime (1998, 2, 28)},
    {"name": "Alex", "birthday": datetime (1988, 7, 29)},
    {"name": "Tabitha", "birthday": datetime (1987, 2, 25)},
    {"name": "Alina", "birthday": datetime (1989, 3, 1)},
    {"name": "Chris", "birthday": datetime (1991, 3, 1)}
     ]

def get_birthdays_per_week (users):
    birthdays_per_week = defaultdict (list)
    
    today = datetime.today().date()

    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()  
        birthday_this_year = birthday.replace (year = today.year)
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace (year = today.year + 1)

        delta_days = (birthday_this_year - today).days

        birthday_weekday = birthday_this_year.strftime ("%A")
                
        if birthday_this_year.weekday () in [5, 6]:
            birthday_this_year += timedelta(days=(7 - birthday_this_year.weekday()))
            birthday_weekday = "Monday"
        
        if delta_days < 7:
            birthdays_per_week [birthday_weekday].append(name)
    
    for weekday, names in birthdays_per_week.items():
        print(f"{weekday}: {', '.join(names)}")
        
    return print


get_birthdays_per_week(users)
    