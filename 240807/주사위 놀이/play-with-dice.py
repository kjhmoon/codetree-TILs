# 배열에 주어진 수를 입력받아 저장
arr = list(map(int, input().split()))
count_arr = [0] * 7
	
# 카운팅 배열을 통해 각각의 빈도 저장
for elem in arr:
	count_arr[elem] += 1
	
# 1부터 6까지 나온 횟수를 출력
for i in range(1, 7):
	print(f"{i} - {count_arr[i]}")