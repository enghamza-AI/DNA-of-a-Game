#DNA of a game

#Create trait names

traits = ["Violence", "Story", "Exploration", "Difficulty"]

#Create vector values

game_vector = [0.2, 0.9, 0.4, 0.6]

#Assuming first trait is strongest

max_value = game_vector[0]
max_index = 0

#Assuming first trait is the weakest its sort of initialization every algorithm need a point to start
min_value = game_vector[0]
min_index = 0

#loop through vector

for i in range(len(game_vector)):
    if game_vector[i] > max_value:
        max_value = game_vector[i]
        max_index = i


for j in range(len(game_vector)):
    if game_vector[j] < min_value:
        min_value = game_vector[j]
        min_index = j


#printing strongest trait and the weakest one

print("Strongest trait is:", traits[max_index])
print("value:", max_value)

print("Weakest trait is:", traits[min_index])
print("value:", min_value)
