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

def solution(number):
    if number < 0:
        return 0  # Return 0 if the number is negative

    count = 0  # Initialize count as an integer for summing
    for i in range(number):  # Use range(number) to iterate up to, but not including, 'number'
        if i % 5 == 0 or i % 3 == 0:  # Check if divisible by 5 or 3
            count += i  # Add the number to the total count
    return count

print(solution(200))











