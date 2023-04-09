with open('D:/Python/Alien invasion/High_score.txt') as file_object:
    high_score = file_object.read()

print(high_score)

filename = 'D:/Python/Alien invasion/High_score.txt'

with open(filename, 'w') as file_object:
    file_object.write('500')