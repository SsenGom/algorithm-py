# 1. 문자와 문자열

print(input()[int(input())-1])


# 2. 단어 길이 재기

print(len(input()))


# 3. 문자열

T = int(input())

for _ in range(T):
    S = input()
    print(f"{S[0]}{S[-1]}")


# 4. 아스키 코드 

print(ord(input()))


# 5. 숫자의 합

N = int(input())
S = input()
a = 0
for i in range(N):
    a += int(S[i])
print (a)


# 6. 알파벳 찾기

다른사람 정답을 훔쳐보니 아스키코드 값을 이용해 풀이하더라.

# 문자열 리스트로 변환
arr = list("abcdefghijklmnopqrstuvwxyz") 
S = input()

# 이중포문으로 (arr이 상수라 성능 문제 없을 듯) 일치하는 값 숫자 대입
for i in S:
    for j in range(len(arr)):
        if i == arr[j]:
            arr[j] = S.index(i) 

# 나머지 str 값들을 -1 로 변경
for i in range(len(arr)):
    if isinstance(arr[i], str):
        arr[i] = -1 

print(*arr)


# 7. 문자열 반복

T = int(input())

for _ in range(T):
    R,S= input().split()
# 리스트를 활용할 경우 조인
    result = []
    for i in S:
        for _ in range(int(R)):
            result.append(i) 
    print("".join(result))

-------------------------------------------

T = int(input())

for _ in range(T):
    R,S= input().split()
#문자열로 바로 처리 가능 end="" 활용
    for i in S:
        print(i*int(R),end="")


# 8. 단어의 갯수

S = input()
# strip으로 앞뒤 공백제거
print(len(S.strip().split()))



# 9. 상수

A, B = input().split()

print(A[::-1] if int(A[::-1]) > int(B[::-1]) else B[::-1])


# 10. 다이얼

손이 아픈 문제

S = list(input())

a = 0
for i in S:
    if i in "ABC":
        a += 3
    elif i in "DEF":
        a += 4
    elif i in "GHI":
        a += 5
    elif i in "JKL":
        a += 6
    elif i in "MNO":
        a += 7    
    elif i in "PQRS":
        a += 8
    elif i in "TUV":
        a += 9
    elif i in "WXYZ":
        a += 10

print(a)


# 11. 그대로 출력하기

import sys

# stdin에서 입력 
for line in sys.stdin:
    print(line, end='')

---------------------------------------------

# input 이용
while True:
    try:
        line = input()  
        print(line)     
    except EOFError:
        break  


sys.stdin을 사용하는 방법은 주로 파일이나 리다이렉션을 통해 입력받을 때 유용하다

