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

def solution(text, ending):
    last_characters = text[-len(ending):]
    # ending_last = ending[-1:]
    if last_characters == ending:
        return True
    else:
        return False

print(solution("sumo", "omo"))














