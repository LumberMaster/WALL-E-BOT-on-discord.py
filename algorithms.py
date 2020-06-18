from random import randint
def Bynary_search(arr, item): # бинарный поиск (массив должен быть отсортирован)
    min = 0
    max = len(arr)
    while min != max:
        mid = int(max/2)
        if item < arr[mid]:
            max = mid
        elif item == arr[mid]:
            return mid
        else:
            min = mid

def create_arr(min = 0,max = 10,n = 10): # создание массива
    A = [0]*n
    for i in range(0,n):
        A[i] = randint(min,max)
    return A

def quick_sort(): # сортировка быстрая
    pass
def bubble_sort(): # сортировка пузырьком
    pass

def selection_sort(arr1): # сортировка выборкой
    n = len(arr1)
    arr2 = [0]*n
    for j in range(0,len(arr1)):
        min = 0
        for i in range(0,len(arr1)):
            if (arr1[i] < arr1[min]):
                min = i
        arr2[j] = arr1[min]
        del arr1[min]
    return arr2


def union_sort(): # сортировка объединением
    pass
a = create_arr(0,10,20)
print(a)
a = selection_sort(a)
print(a)
print(Bynary_search(a,10))