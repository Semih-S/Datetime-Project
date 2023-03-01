import datetime

def days_in_month(year, month):
    """
    Inputs:
      year  - an integer between datetime.MINYEAR and datetime.MAXYEAR
              representing the year
      month - an integer between 1 and 12 representing the month

    Returns:
      The number of days in the input month.
    """
    if month == 1: return 31
    elif (year % 4 != 0) and month == 2: return 28
    elif (year % 4 == 0) and (year % 100 == 0 and year % 400 != 0) and month == 2: return 28
    elif (year % 4 == 0) and month == 2: return 29
    elif month == 3: return 31
    elif month == 4: return 30
    elif month == 5: return 31
    elif month == 6: return 30
    elif month == 7: return 31
    elif month == 8: return 31
    elif month == 9: return 30
    elif month == 10: return 31
    elif month == 11: return 30
    elif month == 12: return 31

#Test
result = days_in_month(5, 2)
print (result)

def is_valid_date(year, month, day):
    """
    Inputs:
      year  - an integer representing the year
      month - an integer representing the month
      day   - an integer representing the day

    Returns:
      True if year-month-day is a valid date and
      False otherwise
    """
    if year < datetime.MINYEAR: return False
    elif year > datetime.MAXYEAR: return False
    elif month > 12: return False
    elif month < 1: return False
    elif (month == 1) and ((day > 31 or day < 1)): return False
    elif (year % 4 != 0) and month == 2 and ((day < 1 or day > 28)): return False
    elif (year % 4 == 0) and (year % 100 == 0 and year % 400 != 0) and month == 2 and ((day < 1 or day > 28)): return False
    elif (year % 4 == 0) and month == 2 and ((day < 1 or day > 29)): return False
    elif month == 3 and ((day > 31 or day < 1)) : return False
    elif month == 4 and ((day > 30 or day < 1)) : return False
    elif month == 5 and ((day > 31 or day < 1)) : return False
    elif month == 6 and ((day > 30 or day < 1)) : return False
    elif month == 7 and ((day > 31 or day < 1)) : return False
    elif month == 8 and ((day > 31 or day < 1)) : return False
    elif month == 9 and ((day > 30 or day < 1)) : return False
    elif month == 10 and ((day > 31 or day < 1)) : return False
    elif month == 11 and ((day > 30 or day < 1)) : return False
    elif month == 12 and ((day > 31 or day < 1)) : return False
    else :return True

#Test
result = is_valid_date(1000, 12, 31)
print (result)

def days_between(year1, month1, day1, year2, month2, day2):
    """
    Inputs:
      year1  - an integer representing the year of the first date
      month1 - an integer representing the month of the first date
      day1   - an integer representing the day of the first date
      year2  - an integer representing the year of the second date
      month2 - an integer representing the month of the second date
      day2   - an integer representing the day of the second date

    Returns:
      The number of days from the first date to the second date.
      Returns 0 if either date is invalid or the second date is
      before the first date.
    """
    if is_valid_date(year1, month1, day1) and is_valid_date(year2, month2, day2) :
        date1 = datetime.date(year1, month1, day1)
        date2 = datetime.date(year2, month2, day2)
        diff = date2 - date1
        if (date2 > date1):
            return (diff.days)
        else:
            return 0
    else:
        return 0
    
#Test 
result = days_between(1600, 10, 12, 2000, 11, 15)
print (result)
    
    
    
    
    
    
    
    
    
    
def age_in_days(year, month, day):
    """
    Inputs:
      year  - an integer representing the birthday year
      month - an integer representing the birthday month
      day   - an integer representing the birthday day

    Returns:
      The age of a person with the input birthday as of today.
      Returns 0 if the input date is invalid or if the input
      date is in the future.
    """
    today = datetime.date.today()
    return days_between(year, month, day, today.year, today.month, today.day)