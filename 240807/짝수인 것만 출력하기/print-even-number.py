# 변수 선언 및 입력
n = int(input())

# 배열에 주어진 수를 입력받아 저장합니다.
arr = list(map(int, input().split()))
new_arr = []
  
# n개의 정수 중 짝수만 새로운 배열에 저장
for elem in arr:
	if elem % 2 == 0:
		new_arr.append(elem)

# n개의 정수 중 짝수만 출력
for elem in new_arr:
	print(elem, end=" ")