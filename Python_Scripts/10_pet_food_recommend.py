pet = input("Enter the pet specie -: ")
pet_age = int(input("Enter the age of the pet -: "))

if pet == "Dog":
    if pet_age < 2:
        food = "Puppy Food"
    else:
        food = "Adult Dog Food"    
elif pet == "Cat":
    if pet_age > 5:
        food ="Senior Cat Food"
    else:
        food = "Junior Cat Food"    
print("Recommended food for your pet",pet, food)                