salary = int(input('Enter the salary amount: '))
years = int(input('Enter the years of service: '))

if years > 5:
    print('You will get a bonus of '+ str(salary*5/100))
else:
    print('You are not eligible for bonus')