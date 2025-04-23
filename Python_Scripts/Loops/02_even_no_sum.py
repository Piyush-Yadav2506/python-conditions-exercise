n = int(input("Enter a number: "))
sum_even_count = 0

for num in range(0, n):
    if num%2 == 0:
        sum_even_count += num
        
print("Sum of even numbers is :", sum_even_count)        