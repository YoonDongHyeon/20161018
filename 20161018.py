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
print(prob)
 # 스트링으로 해야 ans가 스트링이기 때문에 스트링으로 바꿔서 리스트로 변환해줘야한다.

count = 0
while True:
    ans = input("Input number:")
    # 숫자가 안들어오면 다시 입력하게 하는 과정
    if not ans.isdigit():
        print("Please input only number.")
        continue

    count +=1
    strike = 0
    ball = 0

    t = list(set(ans))
    # set 은 그 자체로 갯수를 셀 수 없으므로 리스트로 다시 캐스팅
    # set 은 중복되면 아에 element를 지워버림
    # 버블정렬 찾아볼것!
    if len(t) !=3:
        print(" Do not 중복")
        continue

    # for k in range(0,3):
    #     for l in range(0,3):
    #         if ans[k] == ans [l]:
    #             continue

    for i in range(len(prob)):
        for j in range(len(ans)):
            if i == j and prob[i] == ans[j]:
                strike += 1
            if i !=  j and prob[i] == ans[j]:
                ball += 1
    print("strike is:",strike)
    print("ball is:",ball)

    if strike == 3:
        print("You did.")
        break