import math

def isPrime(num):
    if num <= 1:
        return False
    for div in range(2, int(math.sqrt(num)) + 1):
        if num % div == 0:
            return False
    return True

while True:
    try:
        numberInput = int(input("Enter a number to check if it's prime (or '0' to quit): "))
        if numberInput == 0:
            print("Exiting program. Goodbye!")
            break
        if isPrime(numberInput):
            print(f"{numberInput} is a prime number.")
        else:
            print(f"{numberInput} is not a prime number.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
