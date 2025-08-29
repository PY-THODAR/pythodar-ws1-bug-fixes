# Factorial of a number
n = int(input("Enter a number: "))
fact = 0   
for i in range(1, n+1):
    fact = fact * i
print("Factorial is:", fact)
