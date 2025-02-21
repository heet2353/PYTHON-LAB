#Q.1 Write following programs in Python using If-Condition and Functions
#Print largest and smallest values out of two.

def largest_and_smallest(a, b):
    if a > b:
        largest = a
        smallest = b
    else:
        largest = b
        smallest = a
    
    print(largest)
    print(smallest)

a = float(input())
b = float(input())
largest_and_smallest(a, b)

#Q.2 Write following programs in Python using If-Condition and Functions

Print largest and smallest values out of three.

def largest_and_smallest(a, b, c):
    if a > b and a > c:
        largest = a
    elif b > c:
        largest = b
    else:
        largest = c
    
    if a < b and a < c:
        smallest = a
    elif b < c:
        smallest = b
    else:
        smallest = c
    
    print(largest)
    print(smallest)

a = float(input())
b = float(input())
c = float(input())
largest_and_smallest(a, b, c)

#Q.3 Write following programs in Python using If-Condition and Functions

Check whether a given number is odd or even.

def largest_and_smallest(a, b, c):
    if a > b and a > c:
        largest = a
    elif b > c:
        largest = b
    else:
        largest = c
    
    if a < b and a < c:
        smallest = a
    elif b < c:
        smallest = b
    else:
        smallest = c
    
    print(largest)
    print(smallest)

def check_odd_even(number):
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")

a = float(input())
b = float(input())
c = float(input())
largest_and_smallest(a, b, c)

num = int(input())
check_odd_even(num)

#Q.4 Write following programs in Python using If-Condition and Functions

Check whether a given number is divisible by 10 or not

def largest_and_smallest(a, b, c):
    if a > b and a > c:
        largest = a
    elif b > c:
        largest = b
    else:
        largest = c
    
    if a < b and a < c:
        smallest = a
    elif b < c:
        smallest = b
    else:
        smallest = c
    
    print(largest)
    print(smallest)

def check_odd_even(number):
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")

def check_divisible_by_10(number):
    if number % 10 == 0:
        print("Divisible by 10")
    else:
        print("Not divisible by 10")

a = float(input())
b = float(input())
c = float(input())
largest_and_smallest(a, b, c)

num = int(input())
check_odd_even(num)
check_divisible_by_10(num)

#Q.5 Write following programs in Python using If-Condition and Functions


Accept age of a person. If age is less than 18, print minor otherwise Major.

def largest_and_smallest(a, b, c):
    if a > b and a > c:
        largest = a
    elif b > c:
        largest = b
    else:
        largest = c
    
    if a < b and a < c:
        smallest = a
    elif b < c:
        smallest = b
    else:
        smallest = c
    
    print(largest)
    print(smallest)

def check_odd_even(number):
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")

def check_divisible_by_10(number):
    if number % 10 == 0:
        print("Divisible by 10")
    else:
        print("Not divisible by 10")

def check_age_category(age):
    if age < 18:
        print("Minor")
    else:
        print("Major")

a = float(input())
b = float(input())
c = float(input())
largest_and_smallest(a, b, c)

num = int(input())
check_odd_even(num)
check_divisible_by_10(num)

age = int(input())
check_age_category(age)

#Q.6 Write following programs in Python using If-Condition and Functions


Accept a number from the user. And print number of digits in it.

def largest_and_smallest(a, b, c):
    if a > b and a > c:
        largest = a
    elif b > c:
        largest = b
    else:
        largest = c
    
    if a < b and a < c:
        smallest = a
    elif b < c:
        smallest = b
    else:
        smallest = c
    
    print(largest)
    print(smallest)

def check_odd_even(number):
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")

def check_divisible_by_10(number):
    if number % 10 == 0:
        print("Divisible by 10")
    else:
        print("Not divisible by 10")

def check_age_category(age):
    if age < 18:
        print("Minor")
    else:
        print("Major")

def count_digits(number):
    print(len(str(abs(number))))

a = float(input())
b = float(input())
c = float(input())
largest_and_smallest(a, b, c)

num = int(input())
check_odd_even(num)
check_divisible_by_10(num)

age = int(input())
check_age_category(age)

num_digits = int(input())
count_digits(num_digits)

#Q.7 Write following programs in Python using If-Condition and Functions

Accept a year value from the user. Check whether it is a leap year or not.

def largest_and_smallest(a, b, c):
    if a > b and a > c:
        largest = a
    elif b > c:
        largest = b
    else:
        largest = c
    
    if a < b and a < c:
        smallest = a
    elif b < c:
        smallest = b
    else:
        smallest = c
    
    print(largest)
    print(smallest)

def check_odd_even(number):
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")

def check_divisible_by_10(number):
    if number % 10 == 0:
        print("Divisible by 10")
    else:
        print("Not divisible by 10")

def check_age_category(age):
    if age < 18:
        print("Minor")
    else:
        print("Major")

def count_digits(number):
    print(len(str(abs(number))))

def check_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("Leap Year")
    else:
        print("Not a Leap Year")

a = float(input())
b = float(input())
c = float(input())
largest_and_smallest(a, b, c)

num = int(input())
check_odd_even(num)
check_divisible_by_10(num)

age = int(input())
check_age_category(age)

num_digits = int(input())
count_digits(num_digits)

year = int(input())
check_leap_year(year)

#Q.8 Write following programs in Python using If-Condition and Functions

Check whether a triangle is valid or not, when the three angles of the triangle are entered through the keyboard. A triangle is valid if the sum of all the three angles is equal to 180 degrees.

def largest_and_smallest(a, b, c):
    if a > b and a > c:
        largest = a
    elif b > c:
        largest = b
    else:
        largest = c
    
    if a < b and a < c:
        smallest = a
    elif b < c:
        smallest = b
    else:
        smallest = c
    
    print(largest)
    print(smallest)

def check_odd_even(number):
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")

def check_divisible_by_10(number):
    if number % 10 == 0:
        print("Divisible by 10")
    else:
        print("Not divisible by 10")

def check_age_category(age):
    if age < 18:
        print("Minor")
    else:
        print("Major")

def count_digits(number):
    print(len(str(abs(number))))

def check_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("Leap Year")
    else:
        print("Not a Leap Year")

def check_triangle_validity(angle1, angle2, angle3):
    if angle1 + angle2 + angle3 == 180:
        print("Valid Triangle")
    else:
        print("Invalid Triangle")

a = float(input())
b = float(input())
c = float(input())
largest_and_smallest(a, b, c)

num = int(input())
check_odd_even(num)
check_divisible_by_10(num)

age = int(input())
check_age_category(age)

num_digits = int(input())
count_digits(num_digits)

year = int(input())
check_leap_year(year)

angle1 = int(input())
angle2 = int(input())
angle3 = int(input())
check_triangle_validity(angle1, angle2, angle3)

#Q.9 Write following programs in Python using If-Condition and Functions

Print absolute value of a given number.

def largest_and_smallest(a, b, c):
    if a > b and a > c:
        largest = a
    elif b > c:
        largest = b
    else:
        largest = c
    
    if a < b and a < c:
        smallest = a
    elif b < c:
        smallest = b
    else:
        smallest = c
    
    print(largest)
    print(smallest)

def check_odd_even(number):
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")

def check_divisible_by_10(number):
    if number % 10 == 0:
        print("Divisible by 10")
    else:
        print("Not divisible by 10")

def check_age_category(age):
    if age < 18:
        print("Minor")
    else:
        print("Major")

def count_digits(number):
    print(len(str(abs(number))))

def check_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("Leap Year")
    else:
        print("Not a Leap Year")

def check_triangle_validity(angle1, angle2, angle3):
    if angle1 + angle2 + angle3 == 180:
        print("Valid Triangle")
    else:
        print("Invalid Triangle")

def absolute_value(number):
    print(abs(number))

a = float(input())
b = float(input())
c = float(input())
largest_and_smallest(a, b, c)

num = int(input())
check_odd_even(num)
check_divisible_by_10(num)

age = int(input())
check_age_category(age)

num_digits = int(input())
count_digits(num_digits)

year = int(input())
check_leap_year(year)

angle1 = int(input())
angle2 = int(input())
angle3 = int(input())
check_triangle_validity(angle1, angle2, angle3)

num_abs = float(input())
absolute_value(num_abs)

#Q.10 Write following programs in Python using If-Condition and Functions


Given the length and breadth of a rectangle, write a program to find whether the are of the rectangle is greater than its perimeter

def largest_and_smallest(a, b, c):
    if a > b and a > c:
        largest = a
    elif b > c:
        largest = b
    else:
        largest = c
    
    if a < b and a < c:
        smallest = a
    elif b < c:
        smallest = b
    else:
        smallest = c
    
    print(largest)
    print(smallest)

def check_odd_even(number):
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")

def check_divisible_by_10(number):
    if number % 10 == 0:
        print("Divisible by 10")
    else:
        print("Not divisible by 10")

def check_age_category(age):
    if age < 18:
        print("Minor")
    else:
        print("Major")

def count_digits(number):
    print(len(str(abs(number))))

def check_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("Leap Year")
    else:
        print("Not a Leap Year")

def check_triangle_validity(angle1, angle2, angle3):
    if angle1 + angle2 + angle3 == 180:
        print("Valid Triangle")
    else:
        print("Invalid Triangle")

def absolute_value(number):
    print(abs(number))

def check_rectangle_area_vs_perimeter(length, breadth):
    area = length * breadth
    perimeter = 2 * (length + breadth)
    if area > perimeter:
        print("Area is greater than Perimeter")
    else:
        print("Perimeter is greater than or equal to Area")

a = float(input())
b = float(input())
c = float(input())
largest_and_smallest(a, b, c)

num = int(input())
check_odd_even(num)
check_divisible_by_10(num)

age = int(input())
check_age_category(age)

num_digits = int(input())
count_digits(num_digits)

year = int(input())
check_leap_year(year)

angle1 = int(input())
angle2 = int(input())
angle3 = int(input())
check_triangle_validity(angle1, angle2, angle3)

num_abs = float(input())
absolute_value(num_abs)

length = float(input())
breadth = float(input())
check_rectangle_area_vs_perimeter(length, breadth)

#Q.11 Write following programs in Python using If-Condition and Functions


Given three points (x1,y1), (x2,y2) and (x3,y3), check if all the three points fall on one straight line.

def largest_and_smallest(a, b, c):
    if a > b and a > c:
        largest = a
    elif b > c:
        largest = b
    else:
        largest = c
    
    if a < b and a < c:
        smallest = a
    elif b < c:
        smallest = b
    else:
        smallest = c
    
    print(largest)
    print(smallest)

def check_odd_even(number):
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")

def check_divisible_by_10(number):
    if number % 10 == 0:
        print("Divisible by 10")
    else:
        print("Not divisible by 10")

def check_age_category(age):
    if age < 18:
        print("Minor")
    else:
        print("Major")

def count_digits(number):
    print(len(str(abs(number))))

def check_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("Leap Year")
    else:
        print("Not a Leap Year")

def check_triangle_validity(angle1, angle2, angle3):
    if angle1 + angle2 + angle3 == 180:
        print("Valid Triangle")
    else:
        print("Invalid Triangle")

def absolute_value(number):
    print(abs(number))

def check_rectangle_area_vs_perimeter(length, breadth):
    area = length * breadth
    perimeter = 2 * (length + breadth)
    if area > perimeter:
        print("Area is greater than Perimeter")
    else:
        print("Perimeter is greater than or equal to Area")

def check_collinear(x1, y1, x2, y2, x3, y3):
    if (y2 - y1) * (x3 - x2) == (y3 - y2) * (x2 - x1):
        print("Points are collinear")
    else:
        print("Points are not collinear")

a = float(input())
b = float(input())
c = float(input())
largest_and_smallest(a, b, c)

num = int(input())
check_odd_even(num)
check_divisible_by_10(num)

age = int(input())
check_age_category(age)

num_digits = int(input())
count_digits(num_digits)

year = int(input())
check_leap_year(year)

angle1 = int(input())
angle2 = int(input())
angle3 = int(input())
check_triangle_validity(angle1, angle2, angle3)

num_abs = float(input())
absolute_value(num_abs)

length = float(input())
breadth = float(input())
check_rectangle_area_vs_perimeter(length, breadth)

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())
check_collinear(x1, y1, x2, y2, x3, y3)

#Q.12 Write following programs in Python using If-Condition and Functions


Given the coordinates (x,y) of center of a circle and its radius, determine whether a point lies inside the circle, on the circle or outside the circle. (Hint: Use sqrt( ), pow( )

import math

def largest_and_smallest(a, b, c):
    if a > b and a > c:
        largest = a
    elif b > c:
        largest = b
    else:
        largest = c
    
    if a < b and a < c:
        smallest = a
    elif b < c:
        smallest = b
    else:
        smallest = c
    
    print(largest)
    print(smallest)

def check_odd_even(number):
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")

def check_divisible_by_10(number):
    if number % 10 == 0:
        print("Divisible by 10")
    else:
        print("Not divisible by 10")

def check_age_category(age):
    if age < 18:
        print("Minor")
    else:
        print("Major")

def count_digits(number):
    print(len(str(abs(number))))

def check_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("Leap Year")
    else:
        print("Not a Leap Year")

def check_triangle_validity(angle1, angle2, angle3):
    if angle1 + angle2 + angle3 == 180:
        print("Valid Triangle")
    else:
        print("Invalid Triangle")

def absolute_value(number):
    print(abs(number))

def check_rectangle_area_vs_perimeter(length, breadth):
    area = length * breadth
    perimeter = 2 * (length + breadth)
    if area > perimeter:
        print("Area is greater than Perimeter")
    else:
        print("Perimeter is greater than or equal to Area")

def check_collinear(x1, y1, x2, y2, x3, y3):
    if (y2 - y1) * (x3 - x2) == (y3 - y2) * (x2 - x1):
        print("Points are collinear")
    else:
        print("Points are not collinear")

def check_point_circle(cx, cy, radius, px, py):
    distance = math.sqrt(math.pow(px - cx, 2) + math.pow(py - cy, 2))
    if distance < radius:
        print("Inside the Circle")
    elif distance == radius:
        print("On the Circle")
    else:
        print("Outside the Circle")

a = float(input())
b = float(input())
c = float(input())
largest_and_smallest(a, b, c)

num = int(input())
check_odd_even(num)
check_divisible_by_10(num)

age = int(input())
check_age_category(age)

num_digits = int(input())
count_digits(num_digits)

year = int(input())
check_leap_year(year)

angle1 = int(input())
angle2 = int(input())
angle3 = int(input())
check_triangle_validity(angle1, angle2, angle3)

num_abs = float(input())
absolute_value(num_abs)

length = float(input())
breadth = float(input())
check_rectangle_area_vs_perimeter(length, breadth)

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())
check_collinear(x1, y1, x2, y2, x3, y3)

cx = float(input())
cy = float(input())
radius = float(input())
px = float(input())
py = float(input())
check_point_circle(cx, cy, radius, px, py)

#Q.13 Write following programs in Python using If-Condition and Functions

Convert number 0 to 19 to its equivalent words. E.g. 0 à zero, 19ànineteen.

import math

def largest_and_smallest(a, b, c):
    if a > b and a > c:
        largest = a
    elif b > c:
        largest = b
    else:
        largest = c
    
    if a < b and a < c:
        smallest = a
    elif b < c:
        smallest = b
    else:
        smallest = c
    
    print(largest)
    print(smallest)

def check_odd_even(number):
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")

def check_divisible_by_10(number):
    if number % 10 == 0:
        print("Divisible by 10")
    else:
        print("Not divisible by 10")

def check_age_category(age):
    if age < 18:
        print("Minor")
    else:
        print("Major")

def count_digits(number):
    print(len(str(abs(number))))

def check_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("Leap Year")
    else:
        print("Not a Leap Year")

def check_triangle_validity(angle1, angle2, angle3):
    if angle1 + angle2 + angle3 == 180:
        print("Valid Triangle")
    else:
        print("Invalid Triangle")

def absolute_value(number):
    print(abs(number))

def check_rectangle_area_vs_perimeter(length, breadth):
    area = length * breadth
    perimeter = 2 * (length + breadth)
    if area > perimeter:
        print("Area is greater than Perimeter")
    else:
        print("Perimeter is greater than or equal to Area")

def check_collinear(x1, y1, x2, y2, x3, y3):
    if (y2 - y1) * (x3 - x2) == (y3 - y2) * (x2 - x1):
        print("Points are collinear")
    else:
        print("Points are not collinear")

def check_point_circle(cx, cy, radius, px, py):
    distance = math.sqrt(math.pow(px - cx, 2) + math.pow(py - cy, 2))
    if distance < radius:
        print("Inside the Circle")
    elif distance == radius:
        print("On the Circle")
    else:
        print("Outside the Circle")

def number_to_words(n):
    words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    print(words[n] if 0 <= n <= 19 else "Out of range")

a = float(input())
b = float(input())
c = float(input())
largest_and_smallest(a, b, c)

num = int(input())
check_odd_even(num)
check_divisible_by_10(num)

age = int(input())
check_age_category(age)

num_digits = int(input())
count_digits(num_digits)

year = int(input())
check_leap_year(year)

angle1 = int(input())
angle2 = int(input())
angle3 = int(input())
check_triangle_validity(angle1, angle2, angle3)

num_abs = float(input())
absolute_value(num_abs)

length = float(input())
breadth = float(input())
check_rectangle_area_vs_perimeter(length, breadth)

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())
check_collinear(x1, y1, x2, y2, x3, y3)

cx = float(input())
cy = float(input())
radius = float(input())
px = float(input())
py = float(input())
check_point_circle(cx, cy, radius, px, py)

num_words = int(input())
number_to_words(num_words)

#Q.14 Write following programs in Python using If-Condition and Functions

Accept marks of three subjects. Print total and average along with whether a candidate has passed or fail. If student secures <= 39 marks in any subject, consider him as fail. Also assigned a subject wise grade based on the following table:

import math

def largest_and_smallest(a, b, c):
    if a > b and a > c:
        largest = a
    elif b > c:
        largest = b
    else:
        largest = c
    
    if a < b and a < c:
        smallest = a
    elif b < c:
        smallest = b
    else:
        smallest = c
    
    print(largest)
    print(smallest)

def check_odd_even(number):
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")

def check_divisible_by_10(number):
    if number % 10 == 0:
        print("Divisible by 10")
    else:
        print("Not divisible by 10")

def check_age_category(age):
    if age < 18:
        print("Minor")
    else:
        print("Major")

def count_digits(number):
    print(len(str(abs(number))))

def check_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("Leap Year")
    else:
        print("Not a Leap Year")

def check_triangle_validity(angle1, angle2, angle3):
    if angle1 + angle2 + angle3 == 180:
        print("Valid Triangle")
    else:
        print("Invalid Triangle")

def absolute_value(number):
    print(abs(number))

def check_rectangle_area_vs_perimeter(length, breadth):
    area = length * breadth
    perimeter = 2 * (length + breadth)
    if area > perimeter:
        print("Area is greater than Perimeter")
    else:
        print("Perimeter is greater than or equal to Area")

def check_collinear(x1, y1, x2, y2, x3, y3):
    if (y2 - y1) * (x3 - x2) == (y3 - y2) * (x2 - x1):
        print("Points are collinear")
    else:
        print("Points are not collinear")

def check_point_circle(cx, cy, radius, px, py):
    distance = math.sqrt(math.pow(px - cx, 2) + math.pow(py - cy, 2))
    if distance < radius:
        print("Inside the Circle")
    elif distance == radius:
        print("On the Circle")
    else:
        print("Outside the Circle")

def number_to_words(n):
    words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    print(words[n] if 0 <= n <= 19 else "Out of range")

def calculate_results(m1, m2, m3):
    total = m1 + m2 + m3
    average = total / 3
    status = "Pass" if m1 > 39 and m2 > 39 and m3 > 39 else "Fail"
    grades = []
    for mark in [m1, m2, m3]:
        if mark == -1:
            grades.append("NA")
        elif mark <= 39:
            grades.append("F")
        elif mark <= 44:
            grades.append("P")
        elif mark <= 49:
            grades.append("C")
        elif mark <= 54:
            grades.append("B")
        elif mark <= 59:
            grades.append("B+")
        elif mark <= 69:
            grades.append("A")
        elif mark <= 79:
            grades.append("A+")
        else:
            grades.append("O")
    print(total, average, status, grades)

a = float(input())
b = float(input())
c = float(input())
largest_and_smallest(a, b, c)

num = int(input())
check_odd_even(num)
check_divisible_by_10(num)

age = int(input())
check_age_category(age)

num_digits = int(input())
count_digits(num_digits)

year = int(input())
check_leap_year(year)

angle1 = int(input())
angle2 = int(input())
angle3 = int(input())
check_triangle_validity(angle1, angle2, angle3)

num_abs = float(input())
absolute_value(num_abs)

length = float(input())
breadth = float(input())
check_rectangle_area_vs_perimeter(length, breadth)

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())
check_collinear(x1, y1, x2, y2, x3, y3)

cx = float(input())
cy = float(input())
radius = float(input())
px = float(input())
py = float(input())
check_point_circle(cx, cy, radius, px, py)

num_words = int(input())
number_to_words(num_words)

m1 = int(input())
m2 = int(input())
m3 = int(input())
calculate_results(m1, m2, m3)


