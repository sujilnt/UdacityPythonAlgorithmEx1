# monthdays () => This function retrieves current month.
def monthDays(month):
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return months[month-1]

# getCurrentMonth () => resets the currentMonth if the values exceeds 12 .
def getCurrentMonth(currentMonth):
    return currentMonth if currentMonth <= 12 else 0

# isLeapYear () => Check whether is it leap year or not a leap year
def isLeapYear(year):
    return ((year % 4 == 0) & (year % 100 != 0)) | (year % 400 == 0)

# AddingOneDayIFLeapYear () => This function adds a day if it is a leap year
def AddingOneDayIFLeapYear(year):
    return 1 if isLeapYear(year) else 0

# incrementByOne () => This function increment a number by one.
def incrementByOne(number):
    return number+1

# calcualteTotalMonth () => This function calculate total number of the day per month
def calcualteTotalMonth(currentMonth,month2,noOFDays,currentYear,year2):
    totaldays = noOFDays
    curMonth= currentMonth
    TWELVE=12
    FEBRUARY=2
    monthLimit= month2 if currentYear == year2 else TWELVE
    while(curMonth <= monthLimit ):
        curMonth = getCurrentMonth(curMonth)
        totaldays = totaldays + monthDays(curMonth) + ( AddingOneDayIFLeapYear(currentYear) if(curMonth == FEBRUARY) else 0 )
        #print("totlal days", totaldays, monthDays(curMonth),test)
        curMonth += 1
    return totaldays

# calculateNoofDays () => This function  minuses  total start day(that is day1) in a month -  starting month days.
def calculateNoofDays(day, month):
    totalDays1= monthDays(month)
    return totalDays1 - day
# calculateNoofDays2 () => This gives the exact number of day2.
def calculateNoofDays2(day, month):
    totalDays2 = monthDays(month)
    return totalDays2 - (totalDays2 - day)

# daysBetweenDates (year1, month1, day1, year2, month2, day2 ) => Main Function => This function given no of days between day1 to day2.
def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    noOFDays=0
    currentMonth=month1
    currentYear=year1
    while(currentYear <= year2):
        noOFDays = calcualteTotalMonth(currentMonth, month2, noOFDays,currentYear,year2)
        currentYear += 1
        currentMonth=1
    noOFDays = noOFDays - (monthDays(month1)) - monthDays(month2)
    noOFDays = noOFDays + (calculateNoofDays(day1, month1) + calculateNoofDays2(day2, month2))
    #print("The total number of the Days ", noOFDays)
    return noOFDays
'''
print("==>>",daysBetweenDates(2017, 6, 15, 2017, 8, 15) == 61, 2017, 6, 15, 2017, 8, 15)
print("==>>",daysBetweenDates(2017, 7, 15, 2017, 8, 15) == 31, 2017, 7, 15, 2017, 8, 15)
print("==>>",daysBetweenDates(2019, 1, 30, 2019, 12, 30)== 334, 2019, 1, 30, 2019, 12, 30)
print("==>>",daysBetweenDates(2018, 1, 1, 2019, 12, 30) == 728, 2018, 1, 1, 2019, 12, 30)
print("==>>",daysBetweenDates(2018, 1, 2, 2019, 12, 30) == 727, 2018, 1, 1, 2019, 12, 30)
print("==>>",daysBetweenDates(2017, 12, 30,2017, 12, 30) == 0, 2017, 12, 30,2017, 12, 30)
print("==>>",daysBetweenDates(2012, 6, 29,2013, 6, 29) == 365, 2012, 6, 29,2013, 6, 29)
print("==>>",daysBetweenDates(2012, 2, 1,2019, 12, 30) == 2889, 2012, 2, 1,2019, 12, 30)
'''


def testDaysBetweenDates():
    # test same day
    assert (daysBetweenDates(2017, 12, 30, 2017, 12, 30) == 0)
    # test adjacent days
    assert (daysBetweenDates(2017, 12, 30, 2017, 12, 31) == 1)
    # test new year
    assert (daysBetweenDates(2017, 12, 30, 2018, 1, 1) == 2)
    # test full year difference
    assert (daysBetweenDates(2012, 6, 29, 2013, 6, 29) == 365)
    # multiple year difference
    assert(daysBetweenDates(2012, 2, 1,2019, 12, 30) == 2889)

    print("Congratulations! Your daysBetweenDates")
    print("function is working correctly!")


testDaysBetweenDates()