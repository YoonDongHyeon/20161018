import random
prob_rn = [0, 0, 0]
prob_rn[0] = random.randint(0, 9)
prob_rn[1] = random.randint(0, 9)
while prob_rn[0] == prob_rn[1]:
    prob_rn[1] = random.randint(0, 9)

prob_rn[2] = random.randint(0, 9)
while (prob_rn[0] == prob_rn[2]) or (prob_rn[1] == prob_rn[2]) :
    prob_rn[2] = random.randint(0, 9)

prob = str(prob_rn[0]) + str(prob_rn[1]) + str(prob_rn[2])

ans = input("Input number:")
