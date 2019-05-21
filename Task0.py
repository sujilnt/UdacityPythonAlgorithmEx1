# isLeapYear => check whether if its leap year
def isLeapYear(year):
    return ((year % 4 == 0) & (year % 100 != 0)) | (year % 400 == 0)

# increment => increment by one
def increment(value):
    return value+1

# calculateMonthdays => calculating the month days
def calculateMonthdays(month,year):
    noOfDays = monthDays(month);
    return increment(noOfDays) if(isLeapYear(year) & month == 2 ) else noOfDays

# calculateFinalResult => calculating the final result by subrating from the start date.
def calculateFinalResult(nofDays,day1,day2,month2,month1):
    nofDaysinMonth2= monthDays(month2);
    startingMonthDays = nofDays - nofDaysinMonth2 + differenceInDay2(nofDaysinMonth2, day2)
    totalNoofDays = startingMonthDays - monthDays(month2) + differenceInDay1(monthDays(month1), day1)
    # print("checking the results", totalNoofDays)
    return totalNoofDays

# monthDays => A function that retrieves right number of a days per month
def monthDays(month):
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return months[month-1]

# differenceInDay1() => find the difference of total day in the day1-month minus current day1
def differenceInDay1(month, day):
    # print(month,day)
    return month-day;

# differenceInDay2()=>find the difference of total day in the day2-month minus current day2
def differenceInDay2(daysinmonth,day):
    reducedDays = daysinmonth-day
    return daysinmonth - reducedDays;

# totalDaysMonth ()=> calculating the total number of the days in the month
def totalDaysMonth(currentmonth,year1,month2):
    totalDays = 0
    while currentmonth <= month2:
        totalDays = totalDays + calculateMonthdays(currentmonth, year1)
        currentmonth = currentmonth + 1
    return totalDays

#setMonth () => setting the month
def setMonth(currentyear,year,month2):
    DECEMBER=12
    return DECEMBER if(currentyear!= year) else month2

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """
    Calculates the number of days between two dates.
    """

    # if day and year and month is same then 0  ?
    # if month and year is same then calculate only days
    # if year is same then calcuate and months and date
    noofDays = 0
    print(year1, month1, day1, year2, month2, day2)
    if (year1 == year2) & (month1 == month2) & (day1 != day2):
        noofDays = calculateMonthdays(month1,year1)
    elif (year1 == year2) & (month1 < month2):
       currentMonth = month1
       noofDays= totalDaysMonth(currentMonth,year1,month2)
       noofDays = calculateFinalResult(noofDays, day1, day2, month2, month1)
    else:
        noofDays=0;
        currentYear=year1
        currentMonth=month1
        while currentYear<= year2:
            monthFinal = setMonth(currentYear,year2,month2)
            noofDays= noofDays + totalDaysMonth(currentMonth, currentYear, monthFinal)
            currentYear=currentYear+1;
        #print ("total Number of days",noofDays)


    return 0 if(year1 == year2) & (month1 == month2) & (day1 == day2) else noofDays;




    # TODO - by the end of this lesson you will have
    #  completed this function. You do not need to complete
    #  it yet though!


def testDaysBetweenDates():
    # test same day
    assert (daysBetweenDates(2017, 12, 30, 2017, 12, 30) == 0)
    assert (daysBetweenDates(2017, 6, 30, 2017, 7, 30) == 30)
    assert (daysBetweenDates(2017, 6, 30, 2017, 8, 30) == 61)
    assert (daysBetweenDates(2019, 1, 30, 2019, 12, 30) == 334)

    print("Congratulations! Your daysBetweenDates")
    print("function is working correctly!")

#print(daysBetweenDates(2017, 12, 30, 2017, 12, 30))
#testDaysBetweenDates()
test = daysBetweenDates(2018, 1, 30, 2019, 9, 30)
print("test",test);

#daysBetweenDates(2019, 1, 30, 2019, 12, 30)

