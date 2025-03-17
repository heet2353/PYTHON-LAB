#Q.1 Write a program that defines a function count_lower_upper() that accepts a string and
#calculates the number of uppercase and lowercase alphabets in it.
#It should return these values as a dictionary. Call this function for some sample string. 

def count_lower_upper(s):
    # Initialize counters for lowercase and uppercase letters
    lower_count = 0
    upper_count = 0
    
    # Iterate through each character in the string
    for char in s:
        if char.islower():
            lower_count += 1
        elif char.isupper():
            upper_count += 1
    
    # Return the counts as a dictionary
    return {'lowercase': lower_count, 'uppercase': upper_count}

# Example usage
sample_string = "Hello World! This is Python."
result = count_lower_upper(sample_string)
print(result)

#Q.2 Write a program that defines a function compute() that calculates the value of n + nn + nnn + nnnn,
#where n is digit received by the function. test the function for digits 4 to 7.

def compute(n):
    # Convert n to string to easily repeat digits
    n_str = str(n)
    
    # Calculate the sum of n + nn + nnn + nnnn
    result = int(n_str) + int(n_str * 2) + int(n_str * 3) + int(n_str * 4)
    
    return result

# Test the function for digits 4 to 7
for i in range(4, 8):
    print(f"Result for {i}: {compute(i)}")

#Q.3 Write a program that defines a function create_array() to create and return a 3D array whose dimensions are passed to the function.
# Also initialize each element of this aray to a value passed to the function.
#e.g. create_array(3,4,5,n) where first three arguments are 3D array dimensions and 4th value is for initialing each value of the 3D array.

import numpy as np

def create_array(dim1, dim2, dim3, initial_value):
    # Create a 3D array with the specified dimensions and initialize all elements to initial_value
    array = np.full((dim1, dim2, dim3), initial_value)
    return array

# Example usage:
dim1, dim2, dim3 = 3, 4, 5  # Dimensions of the 3D array
initial_value = 'n'         # Value to initialize each element of the array

result = create_array(dim1, dim2, dim3, initial_value)

print(result)

#Q.4 Write a program that defines a function sum_avg() to accept marks of five subjects and calculates total and average.
#It should return  directly both values.

def sum_avg(marks):
    # Calculate total sum of the marks
    total = sum(marks)
    
    # Calculate the average
    average = total / len(marks)
    
    # Return both the total and average
    return total, average

# Example usage:
marks = [85, 90, 78, 92, 88]  # Marks for five subjects
total, avg = sum_avg(marks)

print(f"Total: {total}")
print(f"Average: {avg}")

#Q.5 Pangram is a sentence that uses every letter of the alphabet.
#Write a program to check whether a given string is pangram or not, through a user-defined function ispangram().
#Test the function with “The quick brown fox jumps over the lazy dog” or “Crazy Fredrick bought many very exquisite opal jewels”.
#Hint: use set() to convert the string into

a set of characters present in the string and use <= to check whether alphaset is a subset of
#the given string.

import string

def ispangram(sentence):
    # Create a set of lowercase alphabets
    alphabet_set = set(string.ascii_lowercase)
    
    # Convert the sentence to lowercase and create a set of characters in the sentence
    sentence_set = set(sentence.lower())
    
    # Check if the sentence set contains all the letters of the alphabet
    return alphabet_set <= sentence_set

# Test the function with example sentences
sentence1 = "The quick brown fox jumps over the lazy dog"
sentence2 = "Crazy Fredrick bought many very exquisite opal jewels"

# Check if the sentences are pangrams
print(f"Is the first sentence a pangram? {ispangram(sentence1)}")
print(f"Is the second sentence a pangram? {ispangram(sentence2)}")


#Q.6 Write a function to create and return a list containing tuples of the form (x,x2,x3) for all x between 1 and
#given ending value (both inclusive).

def create_tuples(end_value):
    # Create a list of tuples (x, x^2, x^3) for x from 1 to end_value (inclusive)
    result = [(x, x**2, x**3) for x in range(1, end_value + 1)]
    return result

# Example usage:
end_value = 5
result = create_tuples(end_value)

print(result)


#Q.7 A palindrome is a word or phrase that reads the same in both directions.
#Write a program that defines a function ispalindrome() which checks whether a given string is a palindrome or not.
#Ignore spaces and case mismatch while checking for palindrome.

def ispalindrome(s):
    # Remove spaces and convert to lowercase for case-insensitive comparison
    cleaned_string = ''.join(s.split()).lower()
    
    # Check if the cleaned string is equal to its reverse
    return cleaned_string == cleaned_string[::-1]

# Example usage:
test_string = "A man a plan a canal Panama"
result = ispalindrome(test_string)

print(f"Is the given string a palindrome? {result}")


#Q.8 Write a program that defines a function convert() that receives a string containing a sequence of whitespace separated words and
#returns a string after removing all duplicate words and sorting them alphanumerically.
#Hint: use set(), list () , sorted(), join().

def convert(s):
    # Split the string into a list of words
    words = s.split()
    
    # Remove duplicates by converting the list into a set
    unique_words = set(words)
    
    # Sort the unique words alphanumerically
    sorted_words = sorted(unique_words)
    
    # Join the sorted words back into a single string and return it
    return ' '.join(sorted_words)

# Example usage:
input_string = "apple banana orange apple grape banana orange"
result = convert(input_string)

print(f"Converted string: {result}")


#Q.9 Write a program that defines a function count_alpha_digits() that accepts a string and calculates the number of alphabets and digits in it.
#It should return these values as a dictionary.

def count_alpha_digits(s):
    # Initialize counters for alphabets and digits
    alpha_count = 0
    digit_count = 0
    
    # Iterate through each character in the string
    for char in s:
        if char.isalpha():  # Check if character is an alphabet
            alpha_count += 1
        elif char.isdigit():  # Check if character is a digit
            digit_count += 1
    
    # Return the counts in a dictionary
    return {'alphabets': alpha_count, 'digits': digit_count}

# Example usage:
input_string = "Hello123 World456!"
result = count_alpha_digits(input_string)

print(result)


#Q.10 Write a program that defines a function called frequency() which computes the frequency of words present in a string passed to it.
#The frequencies should be returned in sorted order of words in the string.

def frequency(s):
    # Split the string into words (assuming words are separated by spaces)
    words = s.split()
    
    # Create a dictionary to store the frequency of each word
    word_count = {}
    
    # Iterate through each word in the list
    for word in words:
        # Convert to lowercase to ensure case-insensitivity
        word = word.lower()
        
        # Update the frequency count of each word in the dictionary
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    
    # Sort the dictionary by word (keys) and return it as a list of tuples
    sorted_word_count = sorted(word_count.items())
    
    return sorted_word_count

# Example usage:
input_string = "apple banana apple orange banana apple"
result = frequency(input_string)

# Printing the sorted frequency of words
for word, count in result:
    print(f"'{word}': {count}")


#Q.11 Write a function create_list() that creates and returns a list which is an intersection of two lists passed to it.

def create_list(list1, list2):
    # Find the intersection of the two lists using set intersection
    intersection = list(set(list1) & set(list2))
    return intersection

# Example usage:
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

result = create_list(list1, list2)
print(f"Intersection of the lists: {result}")

#EXTRA


#Q.1 If a positive integer is entered through the keyword, write a recursive function to obtain the prime factors of the number.

def prime_factors(n, divisor=2):
    # Base case: if n becomes 1, no further division is needed
    if n == 1:
        return []
    
    # If n is divisible by the divisor, add divisor to the result and recurse with the reduced value of n
    if n % divisor == 0:
        return [divisor] + prime_factors(n // divisor, divisor)
    
    # Otherwise, try the next potential divisor
    else:
        return prime_factors(n, divisor + 1)

# Example usage:
num = int(input("Enter a positive integer: "))
print(f"Prime factors of {num} are: {prime_factors(num)}")

# Q. 2 A positive integer is entered through the keyboard. Write a function to find its binary equivalent of this number.

def to_binary(n):
    # Base case: when n is 0 or 1, return it as a string
    if n == 0:
        return '0'
    elif n == 1:
        return '1'
    
    # Recursively call the function and concatenate the remainder (n % 2) at each step
    return to_binary(n // 2) + str(n % 2)

# Example usage:
num = int(input("Enter a positive integer: "))
print(f"Binary equivalent of {num} is: {to_binary(num)}")


# Q.3 A string is entered through the keyboard. Write a recursive function that counts the number of vowels in this string.

def count_vowels(s):
    # Base case: if the string is empty, return 0
    if not s:
        return 0
    
    # Check if the first character is a vowel (either lowercase or uppercase)
    if s[0].lower() in 'aeiou':
        # If it's a vowel, count 1 and recurse for the rest of the string
        return 1 + count_vowels(s[1:])
    
    # If it's not a vowel, just recurse for the rest of the string
    return count_vowels(s[1:])

# Example usage:
input_string = input("Enter a string: ")
print(f"Number of vowels in the string: {count_vowels(input_string)}")


# Q.4 Write a recursive function that reverses the list of numbers that it receives.

def reverse_list(lst):
    # Base case: if the list is empty or has one element, it's already reversed
    if len(lst) == 0 or len(lst) == 1:
        return lst
    
    # Recursive case: reverse the rest of the list and append the first element to the result
    return reverse_list(lst[1:]) + [lst[0]]

# Example usage:
numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
reversed_numbers = reverse_list(numbers)
print(f"Reversed list: {reversed_numbers}")

#Q.5 Calculate ab where a and b received through the keyword using recursion.

def power(a, b):
    # Base case: if the exponent is 0, return 1 (since a^0 = 1)
    if b == 0:
        return 1
    
    # If b is positive, recursively multiply a by the result of power(a, b-1)
    return a * power(a, b - 1)

# Example usage:
a = int(input("Enter the base number (a): "))
b = int(input("Enter the exponent (b): "))
result = power(a, b)
print(f"{a} raised to the power of {b} is: {result}")


#Q.6A list contains some negative and some positive values.
#Write a recursive function that sanitizes the list by replacing all negative numbers with 0.

def sanitize_list(lst):
    # Base case: if the list is empty, return an empty list
    if not lst:
        return []
    
    # If the first element is negative, replace it with 0, otherwise keep the element
    first = 0 if lst[0] < 0 else lst[0]
    
    # Recursively sanitize the rest of the list and combine it with the first element
    return [first] + sanitize_list(lst[1:])

# Example usage:
numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
sanitized_numbers = sanitize_list(numbers)
print(f"Sanitized list: {sanitized_numbers}")


#Q. 7 Write a recursive function to obtain average of all numbers present in a given list.

def average(lst, total=0, count=0):
    # Base case: if the list is empty, return the average
    if not lst:
        return total / count if count != 0 else 0
    
    # Recursive case: add the first element to the total and increase the count
    return average(lst[1:], total + lst[0], count + 1)

# Example usage:
numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
avg = average(numbers)
print(f"The average of the numbers is: {avg}")

# Q.8 Write a recursive function to obtain length of a given string.

def string_length(s):
    # Base case: if the string is empty, its length is 0
    if s == "":
        return 0
    
    # Recursive case: remove the first character and add 1 to the length
    return 1 + string_length(s[1:])

# Example usage:
input_string = input("Enter a string: ")
length = string_length(input_string)
print(f"The length of the string is: {length}")



