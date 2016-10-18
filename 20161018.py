import random
prob = [0, 0, 0]
prob[0] = random.randint(0,9)
prob[1] = random.randint(0,9)
while prob[0] == prob[1]:
    prob[1] = random.randint(0, 9)

prob[2] = random.randint(0,9)
while (prob[0] == prob[2]) or (prob[1] == prob[2]) :
    prob[2] = random.randint(0, 9)