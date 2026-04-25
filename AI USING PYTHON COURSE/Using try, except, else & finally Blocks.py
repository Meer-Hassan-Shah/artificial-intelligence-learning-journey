
num = int(input("Enter a number: "))
print(10 / num)  # This line may raise a ZeroDivisionError if num is 0  


try:
    num = int(input("Enter a number: "))
    print(10 / num)  # This line may raise a ZeroDivisionError if num is 0

except ZeroDivisionError:  # This block will execute if a ZeroDivisionError occurs
    print("You cannot divide by zero. Please enter a non-zero number.")

except ValueError:  # This block will execute if a ValueError occurs (e.g., if the input is not a valid integer)
    print("Invalid input. Please enter a valid integer.")

except Exception as e:  # This block will catch any other exceptions that were not caught by the previous except blocks
    print(f"An unexpected error occurred: {e}")



try:
    print("Running code... ")

except:
    print("error found.")

else:
    print("No error found.")

finally:
    print("Done!")
