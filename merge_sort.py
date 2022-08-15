def merge(A, B):
    C = []
    i = k = 0
    while i < len(A) and k < len(B):
        if A[i] <= B[k]:
            C.append(A[i])
            i += 1
        else:
            C.append(B[k])
            k += 1
    while i < len(A):
        C.append(A[i])
        i += 1
    while k < len(B):
        C.append(B[k])
        k += 1
    return C

def merge_sort(F):
    if len(F) <= 1:
        return F[:]
    else:
        middle = len(F) // 2
        F_left = merge_sort(F[:middle])
        F_right = merge_sort(F[middle:])
        T = merge(F_left, F_right)
        F[:] = T[:]
        return F

# test
# print(merge_sort([101, 55, 12, 26, 54, 165, 18]))
