from datetime import date
def age ():
    year_of_birth= int(input('Enter_year_please:'))
    today_date=date.today().year
    age = today_date - year_of_birth
    if age<18:
        print('minor')
    elif age>=18 and age<=36:
        print('youth')
    else:
        print ('elder')

age()