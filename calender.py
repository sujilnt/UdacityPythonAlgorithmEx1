def monthDays(month):
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return months[month-1]

def getCurrentMonth(currentMonth):
    return currentMonth if currentMonth <= 12 else 0

def isLeapYear(year):
    return ((year % 4 == 0) & (year % 100 != 0)) | (year % 400 == 0)

def AddingOneDayIFLeapYear(year):
    return 1 if isLeapYear(year) else 0;

def incrementByOne(number):
    return number+1;

def calcualteTotalMonth(currentMonth,month2,noOFDays,currentYear):
    totaldays = noOFDays
    curMonth= currentMonth
    while(curMonth <= month2):
        curMonth = getCurrentMonth(curMonth)
        totaldays = totaldays + monthDays(curMonth) + ( AddingOneDayIFLeapYear(currentYear) if(curMonth == 2) else 0 ) ;
        #print("totlal days", totaldays, monthDays(curMonth),test)
        curMonth += 1
    return totaldays

def calculateNoofDays(day, month):
    totalDays1= monthDays(month)
    return (totalDays1 - day) if day > 1 else totalDays1

def calculateNoofDays2(day, month):
    totalDays2=  monthDays(month)
    return totalDays2 - (totalDays2 - day)

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    noOFDays=0
    currentMonth=month1
    currentYear=year1
    while(currentYear <= year2):
        noOFDays = calcualteTotalMonth(currentMonth, month2, noOFDays,currentYear)
        noOFDays = noOFDays - (monthDays(month1)) - monthDays(month2)
        noOFDays= noOFDays + (calculateNoofDays(day1, month1) + calculateNoofDays2(day2, month2))
        currentYear += 1
    print("The total number of the Days ", noOFDays);
    return noOFDays
'''
print(daysBetweenDates(2017, 6, 15, 2017, 8, 15) == 61, 2017, 6, 15, 2017, 8, 15)
print(daysBetweenDates(2017, 7, 15, 2017, 8, 15) == 31, 2017, 7, 15, 2017, 8, 15)
print(daysBetweenDates(2019, 1, 30, 2019, 12, 30)== 334, 2019, 1, 30, 2019, 12, 30)
print(daysBetweenDates(2018, 1, 1, 2019, 12, 30) == 728, 2018, 1, 1, 2019, 12, 30)
'''


print(daysBetweenDates(2018, 1, 2, 2019, 12, 30) == 727, 2018, 1, 1, 2019, 12, 30)


