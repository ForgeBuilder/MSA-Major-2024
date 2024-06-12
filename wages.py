def even_or_odd(value):
    value2 = value/2
    if value2 == round(value2,ndigits=0):
        return "Even"
    else:
        return "Odd"







def positive_bool_input_limited(question,limit): #would be better to give this a maximum.
    while True:
        try:
            output = float(input(question))
            if output >= 0 and (output <= limit or limit == 0):
                return output
            elif output <= limit:
                print(f"Input must be less than {limit}!")
        except:
            print("Enter a positive integer ._.")




Hours = positive_bool_input_limited("How many hours will you work daily? ",24)
Wage = positive_bool_input_limited("What is your hourly wage? ",0)
DaysWorked = positive_bool_input_limited("How many days have you worked? ",365)

print(f"Pay Advice\n-------------")
print(f"Hours Worked: {Hours}")
print(f"Hourly wages: ${Wage:.2f}")


AnualBeforeTax = Hours*Wage*DaysWorked
Taxes = AnualBeforeTax*0.12
AnualAfterTax = AnualBeforeTax - Taxes

print(f"Wages Before Taxes: ${AnualBeforeTax:.2f}")
print(f"Tax Ammount: ${Taxes:.2f}")
print(f"Annual Wage After Taxes: ${AnualAfterTax:.2f}")

input()
stuff = int(input("Give number"))

print(even_or_odd(stuff))












# Ask the user to input from the keyboard for two inputs, 
#   hours worked daily 
#   hourly wage.
# 
# Multiplying hours worked daily and hourly wage will give you the wages earned in a day.
# 
# The two input numbers are not necessarily integers. For example, the user can enter values like 35.5 for hours worked or 17.85 for hourly wage.

# Calculate the yearly wage given the two inputs
# Note that the working hours is daily. Assume the user works 350 days per year and the same amount of hours every day.
# It would help to first write down the mathematical formula needed to calculate the yearly wage
# 12% will be deducted from yearly earnings for taxes
# Print the a Pay Advice containing:
# hours worked
# hourly wage
# wages before taxes
# tax amount
# annual wages after taxes
# money values should be printed with a $ sign and all numbers should be rounded to 2 decimal places







def even_or_odd_bad(value):
    if value == 1:
        return "odd"
    elif value == 2:
        return "even"
    elif value == 3:
        return "odd"
    elif value == 4:
        return "even"
    elif value == 5:
        return "odd"
    elif value == 6:
        return "even"
    elif value == 7:
        return "odd"
    elif value == 8:
        return "even"
    elif value == 9:
        return "odd"
    elif value == 10:
        return "even"
    elif value == 11:
        return "odd"
    elif value == 12:
        return "even"
    elif value == 13:
        return "odd"
    elif value == 14:
        return "even"
    elif value == 15:
        return "odd"
    elif value == 16:
        return "even"
    elif value == 17:
        return "odd"
    elif value == 18:
        return "even"
    elif value == 19:
        return "odd"
    elif value == 20:
        return "even"
    elif value == 21:
        return "odd"