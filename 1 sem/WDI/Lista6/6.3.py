a = [2, 8, 5, 1, 3, 7, 16]

def bubble_sort(a):
    for i in range(len(a)-2):
        for j in range(len(a)-1-i):
            if a[j]>a[j+1]: #instrukcja dominujaca
                a[j], a[j+1] = a[j+1], a[j] 
    return a


print(bubble_sort(a))