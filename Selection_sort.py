def selectionS(a,n):
    for i in range(n):
        imin = i
        for j in range(i+1,n):
            if a[j]<a[imin]:
                imin = j
        a[i],a[imin] = a[imin],a[i]

a = [3,1,4,2,7,6,5]
n = len(a)
selectionS(a,n)
print("The sorted array in ascending order = ",a)