def partition(arr, l, r):
    i = l
    pivot = arr[l]

    for j in range(l + 1, r + 1):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i], arr[l] = arr[l], arr[i]
    return i

def quick_sort(arr, l, r):
    if r - l <= 0:
        return

    pivot = partition(arr, l, r)
    print(arr[pivot], end=' ')

    quick_sort(arr, l, pivot - 1)
    quick_sort(arr, pivot + 1, r)

def main():
    n = int(input())
    arr = list(map(int, input().split()))

    quick_sort(arr, 0, n - 1)
    print()

if __name__ == "__main__":
    main()
