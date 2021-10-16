def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        leap = True
      else:
        leap = False
    else:
      leap = True
  else:
    leap = False
  return leap

def days_in_month(year, month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
  value_of_leap = is_leap(year)
  if (1<= month <= 12):
    if value_of_leap == True:
      days = month_days[month-1]
      return days
    elif value_of_leap == False:
      if month == 2:
        days = int(month_days[month-1] + 1)
        return days
      else:
        days = month_days[month-1]
        return days
  else:
    print("Please enter a valid month.")


#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)













