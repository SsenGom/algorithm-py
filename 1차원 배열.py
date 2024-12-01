#1. 개수 세기

# N개의 정수 입력
N = int(input())

# N 개의 정수 만큼 arr에 값 입력. 아닐 시 다시 입력
while 1:
    arr = list(map(int, input().split()))
    if len(arr) == N:
        break
    print(f"{N}개의 값을 입력해주세요")

# count로 갯수세기
print(arr.count(int(input())))




#2. X 보다 작은 수 

N,X= map(int,input().split())

while 1:
    arr = list(map(int, input().split()))
    if len(arr) == N:
        break
    print(f"{N}개의 값을 입력해주세요")

# for문 사용해 x보다 작은 값 if 문으로 리스트에 담기 -> ' '.join으로 문자열로 만든 리스트 출력값 연결
print(' '.join(map(str, [i for i in arr if i < X])))





#3. 최소, 최대

# N개의 정수 입력
N = int(input())

# N 개의 정수 만큼 arr에 값 입력. 아닐 시 다시 입력
while 1:
    arr = list(map(int, input().split()))
    if len(arr) == N:
        break
    print(f"{N}개의 값을 입력해주세요")

# min max 출력
print(f'{min(arr)} {max(arr)}')




#4. 최댓값 

# 9개의 정수 입력
arr = []
for _ in range(9):
    arr.append(int(input()))

# min index 출력
print(max(arr))
print(arr.index(max(arr))+1)




#5. 공 넣기

#N만큼의 바구니에 M번 공을 넣는 문제. i-j 범위의 바구니에 k 번호의 공을 넣는다. 이 때 각 바구니에 공은 1개만 들어가 중복되면 공을 가장 최근에 넣은 값으로 교체해준다.

N,M = map(int, input().split())
# 배열의 길이 조정 0으로 초기화
arr = [0] * N
# i-j 범위 해당하는 arr[a] 값에 k값 대입
for _ in range(M):
    i, j, k = map(int, input().split())
    for a in range(i-1, j):
        arr[a] = k
# 언패킹 연산자 : print 함수 내에서 사용하면 리스트의 각 요소가 공백으로 구분되어 출력
print(*arr)



#6. 공 교체 

# 위 문제와 다르게 각 바구니에는 N의 공이 순서대로 들어가 있고, N개의 바구니에 대해 M번의 바구니끼리의 공 교환을 구현. 
# 두 바구니의 값을 뒤집는게 포인트인데, 상수 K 를 활용해 변경하였음.  하지만 파이썬에서는 arr[i-1], arr[j-1] = arr[j-1], arr[i-1]  와 같은 다중 할당 기능도 존재한다고 한다.


N,M = map(int, input().split())
arr = []
# 배열의 길이 조정 N!로 초기화
for i in range(N):
    arr.append(i+1)

# 공 교체_ 상수 K 생성해 두 값 교체
for _ in range(M):
    i, j = map(int, input().split())
    K = 0
    K = arr[i-1]
    arr[i-1] = arr[j-1]
    arr[j-1] = K
# 언패킹 연산자 : print 함수 내에서 사용하면 리스트의 각 요소가 공백으로 구분되어 출력
print(*arr)



#7. 과제 안 내신 분..?

# 30까지 상수 리스트
arr = [i+1 for i in range(30)]

# 입력값 리스트에서 28번 제외
for _ in range(28):
    arr.remove(int(input()))

print(arr[0])
print(arr[-1])



#8. 나머지

#원래 0도 나머지로 분류하나? 의문이 들었던 문제 set을 사용해 중복제거하고 출력한다.

arr = []
for _ in range(10):
    N = int(input())
    arr.append(N % 42)  
print(len(set(arr)))



#9. 바구니 뒤집기

#6번 공교체와 비슷한 문제. 공교체는 두 값을 교체했다면, 이 문제는 해당 범위의 값의 순서를 뒤집어야한다.

N,M = map(int,input().split())

arr = [i+1 for i in range(N)]

# reversed 사용해 뒤집기. [(start):(end):-1(step)]를 사용해 슬라이싱 해도 된다. 
for _ in range(M):
    i, j = map(int, input().split())
    arr[i-1:j] = reversed(arr[i-1:j])

print(*arr)



#10. 평균

#성적 올려서 말하기 문제. 학창시절 많이 해보던거라 가볍게 풀었따.

N = int(input())
arr = list(map(int, input().split()))
Marr = max(arr)
# 각 값을 재할당해서 풀었음. 굳이 배열에 다시 안담고 변수에 더했어도 괜찮았을듯 
for i in range(N) :
    arr[i] = arr[i]/Marr*100
print(sum(arr)/N)