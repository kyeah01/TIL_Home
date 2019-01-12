# 리스트의 누적합을 인수로 가지는 리스트 구하기
def cumsum(numbers):
    return [sum(numbers[:count+1]) for count in range(len(numbers))]

print(cumsum([1,2,3]))

# 소수 구하기
def sosu