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
