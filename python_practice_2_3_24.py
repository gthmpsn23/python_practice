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

# You will be given an array a and a value x. All you need to do is check whether the provided array contains the value.

# Array can contain numbers or strings. X can be either.

# Return true if the array contains the value, false if not.

def check(seq, elem):
    for i in seq:
        if i == elem:
            return True
    return False

print(check([66, 101], 66))












