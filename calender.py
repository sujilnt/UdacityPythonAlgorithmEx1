# month_days () => This function retrieves current month.
def month_days(month):
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return months[month-1]


# get_current_month () => resets the currentmonth if the values exceeds 12 .
def get_current_month(currentmonth):
    return currentmonth if currentmonth <= 12 else 0


# isleap_year () => Check whether is it leap year or not a leap year
def isleap_year(year):
    return ((year % 4 == 0) & (year % 100 != 0)) | (year % 400 == 0)


# add_one_day_if_leap_year () => This function adds a day if it is a leap year
def add_one_day_if_leap_year(year):
    return 1 if isleap_year(year) else 0


# increment_by_one () => This function increment a number by one.
def increment_by_one(number):
    return number+1


# calculate_total_month () => This function calculate total number of the day per month
def calculate_total_month(currentmonth, month2, noofdays, currentyear, year2):
    totaldays = noofdays
    curmonth= currentmonth
    TWELVE=12
    FEBRUARY=2
    monthlimit= month2 if currentyear == year2 else TWELVE
    while curmonth <= monthlimit:
        curmonth = get_current_month(curmonth)
        totaldays = totaldays + month_days(curmonth) + (add_one_day_if_leap_year(currentyear) if(curmonth == FEBRUARY) else 0)
        # print("totlal days", totaldays, month_days(curmonth),test)
        curmonth += 1
    return totaldays


# calculate_no_of_days () => This function  minuses  total start day(that is day1) in a month -  starting month days.
def calculate_no_of_days(day, month):
    totaldays1 = month_days(month)
    return totaldays1 - day


# calculate_no_of_days2 () => This gives the exact number of day2.
def calculate_no_of_days2(day, month):
    totaldays2 = month_days(month)
    return totaldays2 - (totaldays2 - day)


# days_between_dates (year1, month1, day1, year2, month2, day2 ) =>
#      Main Function => This function given no of days between day1 to day2.
def days_between_dates(year1, month1, day1, year2, month2, day2):
    noofdays = 0
    currentmonth = month1
    currentyear = year1
    while currentyear <= year2:
        noofdays = calculate_total_month(currentmonth, month2, noofdays, currentyear, year2)
        currentyear += 1
        currentmonth = 1
    noofdays = noofdays - (month_days(month1)) - month_days(month2)
    noofdays = noofdays + (calculate_no_of_days(day1, month1) + calculate_no_of_days2(day2, month2))
    # print("The total number of the Days ", noofdays)
    return noofdays


'''
Different test cases
print("==>>",days_between_dates(2017, 6, 15, 2017, 8, 15) == 61, 2017, 6, 15, 2017, 8, 15)
print("==>>",days_between_dates(2017, 7, 15, 2017, 8, 15) == 31, 2017, 7, 15, 2017, 8, 15)
print("==>>",days_between_dates(2019, 1, 30, 2019, 12, 30)== 334, 2019, 1, 30, 2019, 12, 30)
print("==>>",days_between_dates(2018, 1, 1, 2019, 12, 30) == 728, 2018, 1, 1, 2019, 12, 30)
print("==>>",days_between_dates(2018, 1, 2, 2019, 12, 30) == 727, 2018, 1, 1, 2019, 12, 30)
print("==>>",days_between_dates(2017, 12, 30,2017, 12, 30) == 0, 2017, 12, 30,2017, 12, 30)
print("==>>",days_between_dates(2012, 6, 29,2013, 6, 29) == 365, 2012, 6, 29,2013, 6, 29)
print("==>>",days_between_dates(2012, 2, 1,2019, 12, 30) == 2889, 2012, 2, 1,2019, 12, 30)
'''


def testdays_between_dates():
    # test same day
    assert (days_between_dates(2017, 12, 30, 2017, 12, 30) == 0)
    # test adjacent days
    assert (days_between_dates(2017, 12, 30, 2017, 12, 31) == 1)
    # test new year
    assert (days_between_dates(2017, 12, 30, 2018, 1, 1) == 2)
    # test full year difference
    assert (days_between_dates(2012, 6, 29, 2013, 6, 29) == 365)
    # multiple year difference
    assert(days_between_dates(2012, 2, 1,2019, 12, 30) == 2889)

    print("Congratulations! Your days_between_dates")
    print("function is working correctly!")


testdays_between_dates()