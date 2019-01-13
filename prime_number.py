# def solution(n):
#     sosu = set([i for i in range(2,n+1) 
#                   for j in range(2,i//2+1) if i % j == 0])
#     natural = set(range(2,n+1))
#     answer = len(natural - sosu)
#     return answer

# print(solution(10))

# 돌아가는데 효율성 0점인 코드
 
# def solution(n):
#     sosu = set(range(2,n+1)) - {i for i in range(2,n+1) 
#                  for j in range(2,int(i**0.5)+1) if i % j == 0}
#     print(sosu)
#     return len(sosu)

# print(solution(100))

# def solution(n):
#     sosu = list(range(2,n+1))
#     for x in range(2,n+1):
#         for i in range(2,int(x**0.5)+1):
#             for j in range(2, int(x**0.5)+1):
#                 if i*j in sosu:
#                     sosu.remove(i*j)
#     return sosu

# print(solution(100))

def solution(n):
    in_sosu =set(range(2,int(n**0.5)+1)) - {i for i in range(2,int(n**0.5)+1) 
                       for j in range(2,int(i**0.5)+1) if i % j == 0}
    sosu = set(range(2,n+1)) - {y*x for y in in_sosu for x in range(2,int(n//2))}
    print(in_sosu)
    print(sosu)
    return sosu

print(solution(10))