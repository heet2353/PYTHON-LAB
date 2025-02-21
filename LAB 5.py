#Q.1 Create a list of 5 odd integers using random nos. Similarly create a list of 4 even integers using 
#random nos. Replace the third element of odd integers with a list of 4 even integers. Flattern, sort 
#and print the list. Provide appropriate message at each stage.

import random

odd_list = [random.randrange(1, 100, 2) for _ in range(5)]
even_list = [random.randrange(2, 100, 2) for _ in range(4)]

print("Original odd list:", odd_list)
print("Original even list:", even_list)

odd_list[2] = even_list
print("Odd list after replacing third element with even list:", odd_list)

flattened_list = []
for item in odd_list:
    if isinstance(item, list):
        flattened_list.extend(item)
    else:
        flattened_list.append(item)

flattened_list.sort()
print("Final sorted flattened list:", flattened_list)

#Q.2 Generate 20 random integers and store them in a list. Accept a number from the user and print 
#position of all occurrences of that number in the list

import random

numbers = [random.randint(1, 50) for _ in range(20)]
print("Generated list:", numbers)

search_num = int(input("Enter a number to search: "))

positions = [i for i, num in enumerate(numbers) if num == search_num]

if positions:
    print(f"Occurrences of {search_num} found at positions:", positions)
else:
    print(f"{search_num} not found in the list.")

#Q.3 Generate 50 random numbers in the range 1 and 30. Remove all duplicate values from the lis

import random

numbers = [random.randint(1, 30) for _ in range(50)]
print("Original list:", numbers)

unique_numbers = list(set(numbers))
print("List after removing duplicates:", unique_numbers)

#Q.4 Generate 30 random numbers and put them in a list. Create two more lists – one containing only 
#+ve numbers and another with –ve nos.


import random

numbers = [random.randint(-50, 50) for _ in range(30)]
print("Original list:", numbers)

positive_numbers = [num for num in numbers if num > 0]
negative_numbers = [num for num in numbers if num < 0]

print("Positive numbers list:", positive_numbers)
print("Negative numbers list:", negative_numbers)

#Q.5 A list contains 5 strings. Convert all these strings to uppercase.


strings = ["hello", "world", "python", "list", "uppercase"]
uppercase_strings = [s.upper() for s in strings]
print("Uppercase strings:", uppercase_strings)

#Q.6 Convert list of temperatures in Fahrenheit degrees to equivalent Celsius degrees


fahrenheit_temps = [32, 45, 50, 68, 77, 89, 100]
celsius_temps = [(f - 32) * 5 / 9 for f in fahrenheit_temps]
print("Celsius temperatures:", celsius_temps)

#Q.7 Write a menu-driven program to implement the stack data structure.


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        print(f"{item} pushed onto stack")

    def pop(self):
        if self.is_empty():
            print("Stack is empty, nothing to pop")
        else:
            print(f"Popped item: {self.stack.pop()}")

    def peek(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            print(f"Top item: {self.stack[-1]}")

    def is_empty(self):
        return len(self.stack) == 0

#Q.8 Write a menu-driven program to implement the Queue data structure

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)
        print(f"{item} added to the queue")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty, nothing to dequeue")
        else:
            print(f"Dequeued item: {self.queue.pop(0)}")

    def peek(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            print(f"Front item: {self.queue[0]}")

    def is_empty(self):
        return len(self.queue) == 0

    def display(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            print("Queue elements:", self.queue)

queue = Queue()

while True:
    print("\nQueue Menu:")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        item = input("Enter item to enqueue: ")
        queue.enqueue(item)
    elif choice == 2:
        queue.dequeue()
    elif choice == 3:
        queue.peek()
    elif choice == 4:
        queue.display()
    elif choice == 5:
        print("Exiting program")
        break
    else:
        print("Invalid choice, please try again")

#Q.9 Take two lists of numbers. Create third list of numbers for only those numbers from first list which 
#are not there in 2nd list (use list comprehension).

list1 = [1, 2, 3, 4, 5, 6, 7, 8]
list2 = [3, 5, 7, 9, 11]

list3 = [num for num in list1 if num not in list2]

print("Numbers in first list but not in second list:", list3)




