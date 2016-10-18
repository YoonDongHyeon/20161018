# import random
# prob_rn = [0, 0, 0]
# prob_rn[0] = random.randint(0, 9)
# prob_rn[1] = random.randint(0, 9)
# while prob_rn[0] == prob_rn[1]:
#     prob_rn[1] = random.randint(0, 9)
#
# prob_rn[2] = random.randint(0, 9)
# while (prob_rn[0] == prob_rn[2]) or (prob_rn[1] == prob_rn[2]) :
#     prob_rn[2] = random.randint(0, 9)
#
# prob = str(prob_rn[0]) + str(prob_rn[1]) + str(prob_rn[2])
# print(prob)
#  스트링으로 해야 ans가 스트링이기 때문에 스트링으로 바꿔서 리스트로 변환해줘야한다.
#
# count = 0
# sum_strike = 0
# sum_ball = 0
# while True:
#     ans = input("Input number:")
    # 숫자가 안들어오면 다시 입력하게 하는 과정
    # if not ans.isdigit():
    #     print("Please input only number.")
    #     continue
    #
    # count +=1
    # strike = 0
    # ball = 0
    #
    # avg_strike = 0
    # avg_ball = 0
    # strikes = []
    # balls = []
    # t = list(set(ans))
    # info = []
    # set 은 그 자체로 갯수를 셀 수 없으므로 리스트로 다시 캐스팅
    # set 은 중복되면 아에 element를 지워버림
    # 버블정렬 찾아볼것!
    # if len(t) !=3:
    #     print(" Do not 중복")
    #     continue

    # for k in range(0,3):
    #     for l in range(0,3):
    #         if ans[k] == ans [l]:
    #             continue

    # for i in range(len(prob)):
    #     for j in range(len(ans)):
    #         if i == j and prob[i] == ans[j]:
    #             strike += 1
    #         if i != j and prob[i] == ans[j]:
    #             ball += 1
    # print("strike is:",strike)
    # print("ball is:",ball)

    # sum_strike = sum_strike + strike
    # sum_ball = sum_ball + ball
    # 밑에꺼는 리스트로 평균 스트라이크, 볼 구하는것
    #  strikes.append(strike)
    # balls.append(ball)
    # sum = 0
    # for i in strikes[i]:
    #     sum +=1
    # strike_avg = sum / count

    # sum = 0
    # for j in balls[j]:
    #     sum +=1
    # ball_avg = sum / count
    # info.append(strike,ball)

    # if strike == 3:
    #     print("You did.")
    #     print("Average of strike is",sum_strike/count)
    #     print("Average of ball is",sum_ball/count)
    #     리스트로 한꺼번에 처리하는 방법
    #     sum = [0,0]
    #     for i in range  생각해봐 ㅅㅂ
        # break
    # 버블정렬
    # a = [4,5,7,2,1]
    # for i in range(len(a)-1):
    #     for j in range(i+1,len(a)):
    #         if a[i] > a[j]:
    #             t = a[i]
    #             a[i] = a[j]
    #             a[j] = t
    #
    # print(a)
import random
a=random.randint(0,9)

while True:
    b=random.randint(0,9)
    if a==b:
        continue
    else:
        break
while True:
    c=random.randint(0,9)
    if a==c or b==c:
        continue
    else:
        break
answer = [a,b,c]
print(answer)
while True:
    strike = 0
    ball = 0
    realball = 0
    i = 0
    j = 0
    attack= []
    # hund = int(input("Enter 백의자리 : "))
    # ten = int(input("Enter 십의자리 : "))
    # one = int(input("Enter 일의자리 : "))
    # guess = [hund,ten,one]
    guess = int(input("맞춰보세요! :"))
    if guess > 999 or guess < 0:
        continue
    c = (guess//100)
    d = ((guess//10)%10)
    e = (guess%10)
    attack = [c,d,e]
    print(attack)

    for i in range(0, 3):
        if attack[i]== answer[i]:
            strike+=1
    print('strike is:',strike)

    for i in range(0,3):
        for j in range(0,3):
            if attack[i]==answer[j]:
                ball+=1
    realball = ball - strike

    print('ball is:', realball)
    if strike !=3:
        continue
    else:
        break

print('You are Correct')

