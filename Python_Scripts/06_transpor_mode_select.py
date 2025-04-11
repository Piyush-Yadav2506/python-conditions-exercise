distance = int(input("Enter the distance of your destination -: "))

if distance <= 0:
    mode = "Invalid Input."
elif distance < 3:
    mode = "Walk."
elif distance < 16:
    mode = "Bike."
else:
    mode = "Car."
print("Your mode of transportation -: ", mode)            