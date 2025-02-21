#Q.1 WRITE PYTHON PROGRAMS FOR THE FOLLOWING. (SIMPLE PROGRAMS)
#Add two numbers 

num1 = float(input())
num2 = float(input())
sum = num1 + num2
print(sum)

#Q.2 WRITE PYTHON PROGRAMS FOR THE FOLLOWING. (SIMPLE PROGRAMS)
#Subtract two numbers.

num1 = float(input())
num2 = float(input())
difference = num1 - num2
print(difference)

#Q.3 WRITE PYTHON PROGRAMS FOR THE FOLLOWING. (SIMPLE PROGRAMS)
#Multiply two numbers.

num1 = float(input())
num2 = float(input())
product = num1 * num2
print(product)

#Q.4 WRITE PYTHON PROGRAMS FOR THE FOLLOWING. (SIMPLE PROGRAMS)
#Multiply two numbers

num1 = float(input())
num2 = float(input())
result = num1 / num2 if num2 != 0 else "Cannot divide by zero"
print(result)

#Q.5 WRITE PYTHON PROGRAMS FOR THE FOLLOWING. (SIMPLE PROGRAMS)
#Add, multiply, subtract and divide two numbers 

num1 = float(input())
num2 = float(input())
sum_result = num1 + num2
diff_result = num1 - num2
prod_result = num1 * num2
div_result = num1 / num2 if num2 != 0 else "Cannot divide by zero"
print(sum_result)
print(diff_result)
print(prod_result)
print(div_result)

#Q.6 WRITE PYTHON PROGRAMS FOR THE FOLLOWING. (SIMPLE PROGRAMS)
#Convert hours into minutes. 

hours = float(input())
minutes = hours * 60
print(minutes)

#Q.7 WRITE PYTHON PROGRAMS FOR THE FOLLOWING. (SIMPLE PROGRAMS)
#Convert minutes into hours 

minutes = float(input())
hours = minutes / 60
print(hours)

#Q.8 WRITE PYTHON PROGRAMS FOR THE FOLLOWING. (SIMPLE PROGRAMS)
#onvert dollars into Rs. Where 1 $ = 48 Rs

dollars = float(input())
rupees = dollars * 48
print(rupees)

#Q.9 WRITE PYTHON PROGRAMS FOR THE FOLLOWING. (SIMPLE PROGRAMS)

Convert Rs. into dollars where 1 $ = 48 Rs.

rupees = float(input())
dollars = rupees / 48
print(dollars)


#Q.10 WRITE PYTHON PROGRAMS FOR THE FOLLOWING. (SIMPLE PROGRAMS)
#Convert dollars into pound where 1 $ = 48 Rs. And 1 pound = 70 Rs.

dollars = float(input())
rupees = dollars * 48
pounds = rupees / 70
print(pounds)

#Q.11 WRITE PYTHON PROGRAMS FOR THE FOLLOWING. (SIMPLE PROGRAMS)
#Convert grams into kg

grams = float(input())
kilograms = grams / 1000
print(kilograms)

#Q.12 WRITE PYTHON PROGRAMS FOR THE FOLLOWING. (SIMPLE PROGRAMS)
 #Convert kgs into grams.

kilograms = float(input())
grams = kilograms * 1000
print(grams)

#Q.13 WRITE PYTHON PROGRAMS FOR THE FOLLOWING. (SIMPLE PROGRAMS)
#Convert bytes into KB, MB and GB.

bytes = float(input())
kb = bytes / 1024
mb = kb / 1024
gb = mb / 1024
print(kb, mb, gb)

#Q.14 WRITE PYTHON PROGRAMS FOR THE FOLLOWING. (SIMPLE PROGRAMS)
#Convert celcius into Fahrenheit. F = (9/5 * C) + 32

celsius = float(input())
fahrenheit = (9/5 * celsius) + 32
print(fahrenheit)

#Q.15 WRITE PYTHON PROGRAMS FOR THE FOLLOWING. (SIMPLE PROGRAMS)
#Convert Fahrenheit into celcius. C = 5/9 * (F – 32)

fahrenheit = float(input())
celsius = 5/9 * (fahrenheit - 32)
print(celsius)

#Q.16 WRITE PYTHON PROGRAMS FOR THE FOLLOWING. (SIMPLE PROGRAMS) 
#Calculate area & perimeter of a square. A = L^2, P = 4L

side = float(input())
area = side ** 2
perimeter = 4 * side
print(area)
print(perimeter)

#Q.18 WRITE PYTHON PROGRAMS FOR THE FOLLOWING. (SIMPLE PROGRAMS)
#Calculate area & perimeter of a rectangle. A = L*B, P = 2 (L+B)

length = float(input())
breadth = float(input())
area = length * breadth
perimeter = 2 * (length + breadth)
print(area)
print(perimeter)

#Q.19 WRITE PYTHON PROGRAMS FOR THE FOLLOWING. (SIMPLE PROGRAMS) 
#Calculate area of a circle. A = 22/7 * R * R

radius = float(input())
area = (22/7) * radius * radius
print(area)

#Q.20 WRITE PYTHON PROGRAMS FOR THE FOLLOWING. (SIMPLE PROGRAMS)
#Calculate area of a triangle. A = H*L/2

height = float(input())
length = float(input())
area = (height * length) / 2
print(area)

#Q.21 WRITE PYTHON PROGRAMS FOR THE FOLLOWING. (SIMPLE PROGRAMS)
#Calculate net salary

#where net salary = gross salary + allowance – deduction.
#Allowances are 10% while deductions are 3% of gross salary

gross_salary = float(input())
allowance = 0.10 * gross_salary
deduction = 0.03 * gross_salary
net_salary = gross_salary + allowance - deduction
print(net_salary)

#Q.22 WRITE PYTHON PROGRAMS FOR THE FOLLOWING. (SIMPLE PROGRAMS)
#Calculate net sales where net sales = gross sales – 10% discount of gross sales.

gross_sales = float(input())
discount = 0.10 * gross_sales
net_sales = gross_sales - discount
print(net_sales)

#Q.23 WRITE PYTHON PROGRAMS FOR THE FOLLOWING. (SIMPLE PROGRAMS)
#Calculate average of three subjects along with their total.

subject1 = float(input())
subject2 = float(input())
subject3 = float(input())
total = subject1 + subject2 + subject3
average = total / 3
print(total)
print(average)

#Q.24 WRITE PYTHON PROGRAMS FOR THE FOLLOWING. (SIMPLE PROGRAMS)
#Swap two values.

a = float(input())
b = float(input())
a, b = b, a
print(a)
print(b) 

      
