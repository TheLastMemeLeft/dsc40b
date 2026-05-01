import random


def knn_distance(arr, q, k):
    def partition(lo, hi):
        pivot_idx = random.randint(lo, hi)
        arr[pivot_idx], arr[hi] = arr[hi], arr[pivot_idx]
        pivot_dist = abs(arr[hi] - q)
        i = lo
        for j in range(lo, hi):
            if abs(arr[j] - q) < pivot_dist:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        arr[i], arr[hi] = arr[hi], arr[i]
        return i

    def quickselect(lo, hi, target):
        if lo == hi:
            return arr[lo]
        p = partition(lo, hi)
        if target == p:
            return arr[p]
        elif target < p:
            return quickselect(lo, p - 1, target)
        else:
            return quickselect(p + 1, hi, target)

    point = quickselect(0, len(arr) - 1, k - 1)
    return (abs(point - q), point)
