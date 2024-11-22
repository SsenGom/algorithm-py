1. 두 수 비교하기

A,B = map(int,input().split())

if A > B :
    print('>')
elif A == B :
    print('==')
elif A < B :
    print('<')


2. 시험 성적

A = int(input())

if A <= 100 and A>= 90 :
   print("A")
elif A <= 89 and A>= 80 :
   print("B")
elif A <= 79 and A>= 70 :
   print("C")
elif A <= 69 and A>= 60 :
   print("D")
else:
   print("F")


3. 윤년

A = int(input())

if A%4 == 0 and (A%100 != 0 or A%400 == 0) :
   print("1")
else:
   print("0")


4.사분면 고르기

A = int(input())
B = int(input())

if A>0 and B>0 :
   print("1")
elif A<0 and B>0 :
   print("2")
elif A<0 and B<0 :
   print("3")
elif A>0 and B<0 :
   print("4")   


5. 알람 시계

a,b =map(int,input().split())

if b<45:
    b= 60-(45-b)
    if a-1 <0:
        a= 23
    else:
        a= a-1
else:
    b= b-45
print(a, b)


6. 오븐 시계

A,B = map(int,input().split())
C = int(input())

if B+C>=60:
    A += (B+C)//60
    if A>=24:
        A -= 24
    print(A, (B+C)%60)
else:
    print(A, B+C)
    
-----------------------------------------------

a,b =map(int,input().split())
b += int(input())

print((a+b//60)%24,b%60)


7.주사위 세개

A,B,C = map(int, input().split())

if A==B==C:
    print(10000+A*1000)
elif A==B:
    print(1000+A*100)
elif C==B:
    print(1000+C*100)
elif A==C:
    print(1000+A*100)
else:
    print(max(A,B,C)*100)