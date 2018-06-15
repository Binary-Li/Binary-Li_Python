A=['a','b','c','d','e','f','g','h']
B=A[:]
print(B)

B.append("uu")
A.append("ii")

print(A)
print(B)

print(A[1:])