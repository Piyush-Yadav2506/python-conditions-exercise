order_size = input("Please provide the coffee size -: ")
extra_shot =input("Do you want extra shot of espresso -: ")

if extra_shot == "Yes":
    coffee = order_size + " coffee with an extra shot of espresso"
else:
    coffee = order_size + " coffee"
print("You ordered ",coffee)   