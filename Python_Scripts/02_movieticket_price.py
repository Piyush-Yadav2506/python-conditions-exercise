age = int(input('Enter your Age ='))
day = input('Enter the Day =')

price=12 if age >= 18 else 8
if day == "Wednesday":
    print("Your ticket price is = $", price-2)
else:
    print("Your ticket price is = $",price)    
