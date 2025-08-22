# 10162. 전자레인지

T = int(input())

# 버튼을 누르는 횟수를 최소로 하려면 큰 단위 버튼을 우선순위로
buttons = [300, 60, 10]
cnt =[0, 0, 0]

for i in range(3):
    cnt[i] += T // buttons[i]   # 그 버튼 누른 횟수 = 그 버튼 시간으로 나눈 몫
    T %= buttons[i]

if T>0:             # 남은 시간이 0이 아니면 T초 정확히 맞추기 불가
    ans = [-1]
else:
    ans = cnt


print(*ans)