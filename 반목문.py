1. 구구단

A= int(input())

for i in range(9):
     print( A , "*" , i+1 , "=" , A*(i+1))


2. A+B - 3

A = int(input())
answer =[]

for _ in range(A):
    B, C = map(int,input().split())
    print(B+C)


3. 합

A = int(input())
answer = 0

for i in range(A):
    answer += (i+1)

print(answer)


4. 영수증

A = int(input())
B = int(input())
Asum = 0

for _ in range(B):
    C,D = map(int,input().split())
    Asum += C * D 

if Asum == A:
    print('Yes')
else:
    print('No')


5. 코딩은 체육과목입니다.

#join을 사용해 공백으로 묶어주는 과정 필요.

A = int(input())
Alsit = []

for _ in range(A//4):
    Alsit.append("long")

Alsit.append("int")

print(' '.join(Alsit))


6. 빠른 A+B

#sys.stdin.readline()로 빠른 입력

import sys

A = int(input())
Alist =[]

for _ in range(A):
    B,C =map(int, sys.stdin.readline().split())
    Alist.append(B+C)

for i in Alist:
    print(i)


7. A+B - 7

T = int(input())
Alist = []

for _ in range(T):
    A, B = map(int, input().split())
    Alist.append(A + B)

for i in range(T):
    print(f'Case #{i+1}: {Alist[i]}')


8. A+B - 8

#리스트 하나로 만들어서 하는 방법도 있었을 듯

T = int(input())
Alist = []
Blist = []

for _ in range(T):
    A, B = map(int, input().split())
    Alist.append(A)
    Blist.append(B)

for i in range(T):
    print(f'Case #{i+1}: {Alist[i]} + {Blist[i]} = {Alist[i]+Blist[i]}')


9. 별 찍기 - 1

N = int(input())

for i in range(1, N+1):
    print('*' * i)


10. 별 찍기 - 2

N = int(input())

for i in range(1, N+1):
    print(f'{(N-i)*" "}{i*"*"}')


11. A+B - 5

Alist =[]

while 1:
    A,B = map(int,input().split())
    if A == 0 and B == 0:
        break
    Alist.append(A+B)

    
for i in Alist:
    print(i)


12. A+B - 4

#자꾸 틀려서 이해가 안갔던 문제. 예외 경우를 문제에 표기해주시길 ㅠ

while 1 :
    try:
        A,B = map(int,input().split())
        print(A+B)
    except:
        break;