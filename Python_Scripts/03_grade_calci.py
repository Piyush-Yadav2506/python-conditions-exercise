score = int(input("Enter your final score = "))

if score > 100:
    print("Invalid Input")
    exit()
if score >= 90:
    print("Congratulations\nYou are awarded with GRADE -: A")
elif score >= 80:
    print("Congratulations\nYou are awarded with GRADE -: B")
elif score >= 70:
    print("Congratulations\nYou are awarded with GRADE -: C")
elif score >= 60:
    print("Congratulations\nYou are awarded with GRADE -: D")
else:
    print("Congratulations\nYou are awarded with GRADE -: F")
