#Calculate the multiplication and sum of two numbers 

num1 = float(input("Enter the first number: ")) 

num2 = float(input("Enter the second number: ")) 

multiplication = num1 * num2 

sum = num1 + num2 

print("The multiplication of two numbers is: ", multiplication) 

print("The sum of two numbers is: ",sum) 

 

#Declare two variables and print that which variable is largest using ternary operators 

a = float(input("Enter the first number: ")) 

b = float(input("Enter the second number: ")) 

largest = a if a > b else b 

print("The largest number is: ",largest) 

 

#Python program to convert the temperature in degree centigrade to Fahrenheit 

celsius = float(input("Enter temperature in Celsius: ")) 

fahrenheit = (celsius * 9/5) + 32 

print(celsius,"degree is equal to ",fahrenheit,"degreeF") 

 

#Python program to find the area of a triangle whose sides are given 

base = float(input("Enter the base of the triangle: ")) 

height = float(input("Enter the height of the triangle: ")) 

area = 0.5 * base * height      

print("The area of the triangle is: ",area, "square units") 
