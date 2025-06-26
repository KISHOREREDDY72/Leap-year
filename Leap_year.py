def leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

n = int(input("Enter a year: "))

if leap_year(n):
    print("Leap year")
else:
    print("Not a Leap year")

