# 2차원 배열을 구현합니다.
arr = [
    [0 for _ in range(5)]
    for _ in range(5)
]
	
# 배열의 첫 행과 첫 열을 1로 초기화합니다.
for i in range(5):
	arr[0][i] = 1
	arr[i][0] = 1

# 배열의 숫자를 채웁니다.
for i in range(1, 5):
	for j in range(1, 5):
		arr[i][j] = arr[i - 1][j] + arr[i][j - 1]
		
# 채워진 배열을 출력합니다.
for row in arr:
	for elem in row:
		print(elem, end=" ")
	print()