#========================================================================================================================
#1. Using input() function take one number from the user and using ternary operators
#check whether the number is even or odd

num = int(input("Enter a number: "))
result = "Even" if num % 2 == 0 else "Odd"
print("The", num ,"is",result)
# ========================================================================================================================

#=========================================================================================================================
#2. Using input function take two number and then swap the number. 
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print("Before the swapping: ",num1,"and",num2)
num1, num2 = num2, num1

print("After the swappig: ",num1, "and",num2)
# =========================================================================================================================

#==========================================================================================================================
# 3. Write a Program to Convert Kilometers to Miles

#Take input from the user for kilometers
kilometers = float(input("Enter distance in kilometers: "))

#Conversion factor
conversion_factor = 0.621371

#Convert kilometers to miles
miles = kilometers * conversion_factor

#Print the result
print(f"{kilometers} kilometers is equal to {miles:.2f} miles.")
#============================================================================================================================

#============================================================================================================================
# 4. Find the Simple Interest on Rs. 200 for 5 years at 5% per year.

# # Take input from the user
 principal = float(input("Enter the principal amount (in Rs): "))
 rateofintrest = float(input("Enter the annual interest rate (in %): "))
 time = float(input("Enter the time (in years): "))

# Calculate simple interest
 simple_interest = (principal * rateofintrest * time) / 100

# Print the result
 print(f"The Simple Interest on Rs. {principal} for {time} years at {rateofintrest}% per year is Rs. {simple_interest:.2f}.")
#==============================================================================================================================
#==============================================================================================================================


