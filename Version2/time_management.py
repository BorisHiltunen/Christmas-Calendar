import datetime

#Funktion that returns the date in the correct form
def what_time_is_it(self):
    time = datetime.datetime.now()
    day = time.day
    month = time.month
    year = time.year
    return f"{day}.{month}.{year}"