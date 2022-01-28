a = int(input())

cnt = 0
cnt2 = 0
'''while True:
    if a == 1:
        break

    if a < 1:
        break

    elif a % 2 == 0:
        a = a / 2
        cnt += 1

    elif a % 2 == 1:
        a = a * 3 + 1
        cnt += 1

print(cnt)'''

for i in range(1,a+1):
    if i == 1:
        print()
    elif i == 2:
        cnt += 1
    else:
        for j in range(2, i):
            if i % j == 0:
                cnt2 += 1
        if cnt2 >= 2:
            cnt2 = 0
        elif cnt2 == 1:
            cnt += 1
            cnt2 = 0
        else:
            cnt2 = 0

print(cnt)

