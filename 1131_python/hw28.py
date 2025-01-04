A, B, X, Y = (input() for _ in range(4))
C = A + " " + B
print(C)

D_list = [Y if X.upper() == word.upper() else word for word in C.split()]
D = " ".join(D_list)
print(D)
print(len(C.replace(" ", "")), len(D.replace(" ", "")))

D_rev_list = [
    Y[::-1] if X.upper() == word.upper() else word for word in C.split()
]
D_rev = " ".join(D_rev_list)
print(D_rev)

diff = abs(len(X) - len(Y))
print(C[::diff])
