import random
legal_moves = ["R", "R'", "L", "L'", "U", "U'", "D", "D'", "F", "F'", "B", "B'"]
rand_moves = []
ind = []
num_moves = int(input("Enter number of random moves you want to generate: "))
for i in range(num_moves):
  ind.append(random.randint(0,11))

for i in ind:
  rand_moves.append(legal_moves[i])

print("Generated scramble:")
print(" ".join(rand_moves))