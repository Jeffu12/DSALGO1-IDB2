#1 Bubble Sort Ascending
def BubbleSortAsc(arr1):
    print("Array 1 before Bubble Sort ascending order: ", arr1)
    for i in range(len(arr1)):
        for j in range(0, len(arr1) - i - 1):
            if arr1[j] > arr1[j + 1]:
                arr1[j], arr1[j + 1] = arr1[j + 1], arr1[j]
    print("Array 1 after Bubble Sort ascending order: ", arr1)
    print()


#2 Insertion Sort Ascending
def InsertionSortAsc(arr2):
    print("Array 2 before Insertion Sort ascending order: ", arr2)
    for i in range(1, len(arr2)):
        key = arr2[i]
        j = i - 1
        while j >= 0 and key < arr2[j]:
            arr2[j + 1] = arr2[j]
            j -= 1
        arr2[j + 1] = key
    print("Array 2 after Insertion Sort ascending order: ", arr2)
    print()


#3 Selection Sort Descending
def SelectionSortDesc(arr3):
    print("Array 3 before Selection Sort descending order: ", arr3)
    for i in range(len(arr3)):
        min_idx = i
        for j in range(i + 1, len(arr3)):
            if arr3[min_idx] < arr3[j]:
                min_idx = j
        arr3[i], arr3[min_idx] = arr3[min_idx], arr3[i]
    print("Array 3 after Selection Sort descending order: ", arr3)
    print()


#4 Insertion Sort Descending
def InsertionSortDesc(arr4):
    print("Array 4 before Insertion Sort descending order: ", arr4)
    for i in range(1, len(arr4)):
        key = arr4[i]
        j = i - 1
        while j >= 0 and key > arr4[j]:
            arr4[j + 1] = arr4[j]
            j -= 1
        arr4[j + 1] = key
    print("Array 4 after Insertion Sort descending order: ", arr4)
    print()


#5
def AscAndDesc(arr5):
    desc = []
    asc = []
    asc = arr5.copy()
    desc = arr5.copy()
    print("Array 5 before Ascending & Descending: ", arr5)
    for i in range(len(asc)):
        for j in range(0, len(asc) - i - 1):
            if asc[j] > asc[j + 1]:
                asc[j], asc[j + 1] = asc[j + 1], asc[j]
    print("Array 5 After Ascending: ", asc)
    for i in range(len(desc)):
        for j in range(0, len(desc) - i - 1):
            if desc[j] < desc[j + 1]:
                desc[j], desc[j + 1] = desc[j + 1], desc[j]
    print("Array 5 After Descending: ", desc)
    print()
#6
def AllSelectionAsc(arr6):
    print("Array 6 before Selection Sort ascending order: ", arr6)
    for i in range(len(arr6)):
        min_idx = i
        for j in range(i + 1, len(arr6)):
            if arr6[min_idx] > arr6[j]:
                min_idx = j
        arr6[i], arr6[min_idx] = arr6[min_idx], arr6[i]
    print("Array 6 after Selection Sort ascending order: ", arr6)
    print()


#7 Even Odd
def EvenOdd(evenodd):
    even = [num for num in evenodd if num % 2 == 0]
    odd = [num for num in evenodd if num % 2 != 0]
    print("Even Numbers: ", even)
    print("Odd Numbers: ", odd)

arr1 = [23, 89, 7, 56, 44]
BubbleSortAsc(arr1)
arr2 = [12, 78, 91, 34, 62]
InsertionSortAsc(arr2)
arr3 = [5, 99, 48, 15, 67]
SelectionSortDesc(arr3)
arr4 = [38, 82, 25, 74, 13]
InsertionSortDesc(arr4)
arr5 = [7, 56, 91, 34, 48, 15, 25, 74]
AscAndDesc(arr5)
arr6 = [23, 89, 7, 56, 44, 12, 78, 91, 34, 62, 5, 99, 48, 15, 67,38, 82, 25, 74, 13]
AllSelectionAsc(arr6)
EvenOdd(arr6)