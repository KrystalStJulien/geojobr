import datetime
import time

def calculate_date(date):
    #someday = time.strptime("Tue, 11 Jun 2011 05:23:24 GMT", "%a, %d %b %Y %H:%M:%S %Z")
    someday = time.strptime(date, "%a, %d %b %Y %H:%M:%S %Z")
    #struct_time = time.strptime("30 Nov 00", "%d %b %y") 
    day = datetime.date(someday[0], someday[1], someday[2])
    today = datetime.date.today()
    return (today - day).days

