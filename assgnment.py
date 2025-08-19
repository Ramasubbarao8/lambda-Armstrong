#by use while condition
num = int(input("Enter a number: "))
power = len(str(num))  
sum_of_digits = 0
temp = num

while temp > 0:
    digit = temp % 10
    sum_of_digits += digit ** power
    temp //= 10

if num == sum_of_digits:
    print(num, "is an Armstrong number.")
else:
    print(num, "is NOT an Armstrong number.")


# Armstrong Number Program def funtion

def is_armstrong(num):
    
    digits = str(num)
    n = len(digits)
    total = sum(int(digit) ** n for digit in digits)
    
    return total == num

num = int(input("Enter a number: "))

if is_armstrong(num):
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")


# Armstrong number check using lambda
is_armstrong = lambda num: num == sum(int(digit) ** len(str(num)) for digit in str(num))
num = int(input("Enter a number: "))
print(f"{num} is an Armstrong number" if is_armstrong(num) else f"{num} is not an Armstrong number")

    

