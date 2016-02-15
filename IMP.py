import calendar
day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))
#Write your code here

day_name = calendar.weekday(year, month, day)

if (day_name == 0):
    day_name = "Monday"
if  (day_name == 1):   
    day_name = "Tuesday"
if  (day_name == 2):    
    day_name = "Wednesday"
if  (day_name == 3):
    day_name = "Thorsday"
if  (day_name == 4):    
    day_name = "Fryday"
if  (day_name == 5):  
     day_name = "Saturday"
if  (day_name == 6):   
     day_name = "Sunday"
#
print('The day is:',day_name)
