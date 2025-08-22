# 28702. FiZZBuzz

s1 = input()
s2 = input()
s3 = input()

# 입력받은 값 3개 중에 숫자가 있다면, 그 값을 토대로
# 다음으로 나올 숫자를 찾아 규칙에 맞게 출력하면 됨
if s1.isnumeric():
    target = int(s1) +3
elif s2.isnumeric():
    target = int(s2) + 2
elif s3.isnumeric():
    target = int(s3) + 1

# 입력받은 값이 모두 문자라면, 다양한 경우의 수가 있을 수 있지만
# 항상 그 다음 값이 'Fizz'일 수 있음; 무조건 Fizz 출력 
else:
    ans = 'Fizz'

# 입력받은 값 중에 숫자가 있을 때 규칙에 맞게 출력값 정하기 
if target%3==0 and target%5==0:
    ans = 'FizzBuzz'
elif target%3==0:
    ans = 'Fizz'
elif target%5==0:
    ans = 'Buzz'
else:
    ans = target

print(ans)