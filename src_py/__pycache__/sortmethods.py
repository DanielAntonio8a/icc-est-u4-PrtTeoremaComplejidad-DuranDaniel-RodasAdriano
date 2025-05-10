class SortMethods:
    def __init__(self):
        pass

    def bubble_sort(arr):
        a = arr.copy()
        n = len(a)
        for i in range(n):
            for j in range(0, n - i - 1):
                if a[j] > a[j + 1]:
                    a[j], a[j + 1] = a[j + 1], a[j]
        return a

    def bubble_improved_sort(arr):
        a = arr.copy()
        n = len(a)
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                if a[j] > a[j + 1]:
                    a[j], a[j + 1] = a[j + 1], a[j]
                    swapped = True
            if not swapped:
                break
        return a

    def selection_sort(arr):
        a = arr.copy()
        for i in range(len(a)):
            min_idx = i
            for j in range(i + 1, len(a)):
                if a[j] < a[min_idx]:
                    min_idx = j
            a[i], a[min_idx] = a[min_idx], a[i]
        return a

    def insertion_sort(arr):
        a = arr.copy()
        for i in range(1, len(a)):
            key = a[i]
            j = i - 1
            while j >= 0 and key < a[j]:
                a[j + 1] = a[j]
                j -= 1
            a[j + 1] = key
        return a

    def shell_sort(arr):
        a = arr.copy()
        n = len(a)
        gap = n // 2
        while gap > 0:
            for i in range(gap, n):
                temp = a[i]
                j = i
                while j >= gap and a[j - gap] > temp:
                    a[j] = a[j - gap]
                    j -= gap
                a[j] = temp
            gap //= 2
        return a
