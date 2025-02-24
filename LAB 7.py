#Q.1 Write a program to create three dictionaries and concatenate them to create fourth dictionary.

# Creating three dictionaries
dict1 = {"name": "Alice", "age": 25}
dict2 = {"city": "New York", "country": "USA"}
dict3 = {"job": "Engineer", "company": "TechCorp"}

# Concatenate the dictionaries to create a fourth dictionary
dict4 = {**dict1, **dict2, **dict3}

# Display the resulting fourth dictionary
print("Concatenated Dictionary:", dict4)

#Q.2 Write a program to check whether a dictionary is empty or not.

# Creating a dictionary
my_dict = {}

# Check if the dictionary is empty
if not my_dict:
    print("The dictionary is empty.")
else:
    print("The dictionary is not empty.")

#Q.3 Create a dictionary with dept no, employee roll no. and salary. Find out department wise min and maximum of salary

# Creating a dictionary with department number, employee roll number, and salary
employees = {
    101: [(1, 5000), (2, 6000), (3, 7000)],  # Department 101: (roll_no, salary)
    102: [(4, 8000), (5, 5500), (6, 9000)],  # Department 102: (roll_no, salary)
    103: [(7, 7500), (8, 6500), (9, 7200)],  # Department 103: (roll_no, salary)
}

# Dictionary to store min and max salaries department wise
dept_salary_stats = {}

# Loop through each department
for dept_no, employees_list in employees.items():
    # Extracting the salaries of employees in the department
    salaries = [salary for roll_no, salary in employees_list]
    
    # Finding the min and max salary
    min_salary = min(salaries)
    max_salary = max(salaries)
    
    # Storing the result in dept_salary_stats
    dept_salary_stats[dept_no] = {"min_salary": min_salary, "max_salary": max_salary}

# Display the department-wise min and max salary
for dept_no, stats in dept_salary_stats.items():
    print(f"Department {dept_no}: Min Salary = {stats['min_salary']}, Max Salary = {stats['max_salary']}")

#Q.4 Write a program that reads a string from the keyboard and creates dictionary containing frequency of each character occurring in the string.


# Read a string from the user
input_string = input("Enter a string: ")

# Create an empty dictionary to store the frequency of each character
char_frequency = {}

# Loop through each character in the string
for char in input_string:
    if char in char_frequency:
        # If the character is already in the dictionary, increment its count
        char_frequency[char] += 1
    else:
        # If the character is not in the dictionary, add it with a count of 1
        char_frequency[char] = 1

# Display the character frequency dictionary
print("Character frequencies:", char_frequency)

#Q.5 Create two dictionaries – one containing grocery items and their prices and another containing grocery items and quantity purchased.
#By using the values from these two dictionaries compute the total bill.

# Dictionary with grocery items and their prices
grocery_prices = {
    "apple": 2.5,   # Price per apple
    "banana": 1.2,  # Price per banana
    "carrot": 0.8,  # Price per carrot
    "milk": 1.5,    # Price per milk (per liter)
    "bread": 2.0    # Price per bread loaf
}

# Dictionary with grocery items and their quantities purchased
grocery_quantities = {
    "apple": 3,     # 3 apples
    "banana": 5,    # 5 bananas
    "carrot": 4,    # 4 carrots
    "milk": 2,      # 2 liters of milk
    "bread": 1      # 1 loaf of bread
}

# Initialize a variable to store the total bill
total_bill = 0

# Loop through the grocery items and compute the total bill
for item in grocery_prices:
    if item in grocery_quantities:
        # Multiply price by quantity and add to total_bill
        total_bill += grocery_prices[item] * grocery_quantities[item]

# Display the total bill
print(f"The total bill is: ${total_bill:.2f}")


