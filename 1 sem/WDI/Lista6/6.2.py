a = [2, 8, 5, 1, 3, 7]

def selection_sort(a):
    for i in range(len(a)-2):
        min = i
        for j in range(i, len(a)-1):
            if a[j]<a[min]: #instrukcja dominujaca
                min = j 
        if min != i:
            a[min], a[i] = a[i], a[min]
    return a


print(selection_sort(a))