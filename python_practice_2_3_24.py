# Function that calculates the points accumilated by football team over a season 

# def points(games):
#     points = 0
#     for game in games:
#         x , y = game.split(':')
#         x = int(x)
#         y = int(y)
#         if x > y:
#             points += 3
#         elif x < y:
#             continue
#         else:
#             points += 1
#     return points

# print(points(['1:0','2:0','3:0','4:0','2:1','3:1','4:1','3:2','4:2','4:3']))

# String ends with?

# def solution(text, ending):
#     last_characters = text[-len(ending):]
#     if last_characters == ending:
#         return True
#     else:
#         return False

# print(solution("sumo", "omo"))

# You only need one - Beginner

# def check(seq, elem):
#     for i in seq:
#         if i == elem:
#             return True
#     return False

# print(check([66, 101], 66))

# def reverse_seq(n):
#     return list(range(n, 0, -12))
    
# print(reverse_seq(100))

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
# The sum of these multiples is 23.

# Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.

# Additionally, if the number is negative, return 0.

# Note: If the number is a multiple of both 3 and 5, only count it once.

# Courtesy of projecteuler.net (Problem 1)

# def solution(number):
#     if number < 0:
#         return 0  # Return 0 if the number is negative

#     count = 0  # Initialize count as an integer for summing
#     for i in range(number):  # Use range(number) to iterate up to, but not including, 'number'
#         if i % 5 == 0 or i % 3 == 0:  # Check if divisible by 5 or 3
#             count += i  # Add the number to the total count
#     return count

# print(solution(200))

# def generate_hashtag(s):
#     # Step 1: Trim leading/trailing spaces and split into words
#     words = s.strip().split()
    
#     # Step 2: Capitalize the first letter of each word and concatenate
#     hashtag = '#' + ''.join(word.capitalize() for word in words)
    
#     # Step 3 & 4: Check if the result meets the criteria
#     if 1 < len(hashtag) <= 140:
#         return hashtag
#     else:
#         return False


# print(generate_hashtag(" Hello there thanks for trying my Kata"))  # "#HelloThereThanksForTryingMyKata"
# print(generate_hashtag("    Hello     World   "))  # "#HelloWorld"
# print(generate_hashtag(""))  # False

# def create_phone_number(n):
#     return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)

# # Example usage
# print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))  # => returns "(123) 456-7890"

# def reverse_words(text):
#   return text[::-1]

# print(reverse_words("double  spaced  words"))

# def divide(num1, num2):
#     return num1/num2

# num1 = int(input("Please enter a number: "))
# num2 = int(input("Please enter a number: "))

# print(divide(num1,num2))

# def divide(num1, num2):
#     result = 0
#     try:
#         result = num1/num2
#     except ZeroDivisionError:
#         print("Don't divide by zero dickhead!")
#     return result

# num1 = int(input("Please enter a number: "))
# num2 = int(input("Please enter a number: "))
# result = divide(num1,num2)
# print(result)

# def validate_num_input(user_input):
#     try:
#         user_input = int(user_input)
#     except ValueError:
#         print("Invalid input")
#         return None
#     else:
#         return user_input
    
# names = ["Mike", "Peter", "Michelle", "Tina"]

# print("Please choose a name below:")
# for i, name in enumerate(names):
#     print(i, name, sep=". ")

# user_choice = input(": ")
# user_choice = validate_num_input(user_choice)

# if isinstance(user_choice, int) and 0 <= user_choice < len(names):
#     print(f"Selected Name: {names[user_choice]}")
# else:
#     print("Invalid choice")

# """ Given an array of integers, return a new array with each value doubled.

# For example:

# [1, 2, 3] --> [2, 4, 6]"""

# def maps(a):
#     doubled = []
#     for i in a:
#         doubled.append(i * 2)
#     return doubled
    
# print(maps([1,2,3]))


""" Trolls are attacking your comment section!

A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.

Your task is to write a function that takes a string and return a new string with all vowels removed.

For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".

Note: for this kata y isn't considered a vowel."""        

# def disemvowel(string_):
#     new_string = ""
#     for letter in range(len(string_)):
#         if letter == "aeiou":
#             remove
#     return string_
    
# def disemvowel(string_):
#     new_string = ""
#     for letter in string_:  # Iterate over characters directly
#         if letter.lower() not in "aeiou":  # Check if the letter is not a vowel (consider case)
#             new_string += letter  # Add non-vowel characters to the new string
#     return new_string

# print(disemvowel("You're a cunt!"))

# def double_char(s):
#     new_string = ""
#     for letter in s:
#         new_string += letter
#         new_string += letter
#     return new_string

# print(double_char("cunt"))


# def find_average(numbers):
#     sum = 0
#     count = 0
#     for number in numbers:
#         sum += number
#         count += 1

#     try:   
#         average = sum / count
#     except ZeroDivisionError:
#         return 0    
    
#     return average

# print(find_average([0]))

# numbers = [1,4,5,7,3,2,5532234]
# sum(numbers)
# print(sum(numbers))
# len(numbers)
# print(len(numbers))

# average = sum(numbers) / len(numbers)

# print(average)

#         test.assert_equals(twice_as_old(36,7) , 22)
#         test.assert_equals(twice_as_old(55,30) , 5)
#         test.assert_equals(twice_as_old(42,21) , 0)
#         test.assert_equals(twice_as_old(22,1) , 20)
#         test.assert_equals(twice_as_old(29,0) , 29)


def twice_as_old(dad_years_old, son_years_old):
    twice = son_years_old * 2 
    years = dad_years_old - twice
    if years < 0:
        years = abs(years)
    return years

print(twice_as_old(55,30))

    