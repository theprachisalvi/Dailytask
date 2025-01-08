#========================================================================================================================
# Python program to check leap year
# Take input from the user
year = int(input("Enter a year: "))

# Check if the year is a leap year
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
# ========================================================================================================================

#=========================================================================================================================
# Python Program to Find the Largest Among Three Numbers

# Take input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Find the largest number
if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

# Display the result
print(f"The largest number is: {largest}")

# =========================================================================================================================

#==========================================================================================================================
# Python Program to Check if a Number is Positive, Negative or 0

# Take input from the user
number = float(input("Enter a number: "))

# Check if the number is positive, negative, or zero
if number > 0:
    print(f"{number} is a positive number.")
elif number < 0:
    print(f"{number} is a negative number.")
else:
    print("The number is zero.")

#============================================================================================================================

#============================================================================================================================
# A toy vendor supplies three types of toys: Battery Based Toys, Key-based
# Toys, and Electrical Charging Based Toys. The vendor gives a discount of
# 10% on orders for battery-based toys if the order is for more than Rs. 1000.
# On orders of more than Rs. 100 for key-based toys, a discount of 5% is
# given, and a discount of 10% is given on orders for electrical charging based
# toys of value more than Rs. 500. Assume that the numeric codes 1,2 and 3
# are used for battery based toys, key-based toys, and electrical charging based
# toys respectively. Write a program that reads the product code and the order
# amount and prints out the net amount that the customer is required to pay
# after the discount 

# Take input from the user
product_code = int(input("Enter the product code (1 for Battery Based, 2 for Key-Based, 3 for Electrical Charging Based): "))
order_amount = float(input("Enter the order amount: "))

# Initialize discount
discount = 0

# Determine the discount based on product code and order amount
if product_code == 1:  # Battery Based Toys
    if order_amount > 1000:
        discount = 0.10  # 10% discount
elif product_code == 2:  # Key-Based Toys
    if order_amount > 100:
        discount = 0.05  # 5% discount
elif product_code == 3:  # Electrical Charging Based Toys
    if order_amount > 500:
        discount = 0.10  # 10% discount
else:
    print("Invalid product code. Please enter 1, 2, or 3.")
    exit()

# Calculate the net amount
net_amount = order_amount - (order_amount * discount)

# Print the net amount
print(f"The net amount to be paid is: Rs. {net_amount:.2f}")

#==============================================================================================================================
#==============================================================================================================================
# A transport company charges the fare according to following table:
# Distance Charges
# 1-50 8 Rs./Km
# 51-100 10 Rs./Km
# > 100 12 Rs/Km

# Take input from the user
distance = float(input("Enter the distance traveled in kilometers: "))

# Calculate the fare based on the distance
if distance >= 1 and distance <= 50:
    fare = distance * 8  # Rs. 8 per km
elif distance > 50 and distance <= 100:
    fare = distance * 10  # Rs. 10 per km
elif distance > 100:
    fare = distance * 12  # Rs. 12 per km
else:
    print("Invalid distance entered.")
    exit()

# Print the total fare
print(f"The total fare for {distance} km is: Rs. {fare:.2f}")

