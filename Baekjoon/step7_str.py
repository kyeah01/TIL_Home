# print(ord(input()))

# # 10809. 알파벳찾기

# S = input()
# value = 0
# B =[]
# A = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

# for i in range(len(A)):
#     for j in range(len(S)):
#         if S[j]==A[i]:
#             value = j
#             break
#     else:
#         value = -1
#     B.append(value)
# print(*B)

# 2675. 문자열 반복

import sys

T = int(input())
C = T
A = []

while C:
    A.append(sys.stdin.readline().split())
    C -= 1
    if C == 0 : break
for i in range(T):
    for j in range(len(A[i][1])):
        A[i][1] = A[i][1][j] *A[i][0]
print(A)