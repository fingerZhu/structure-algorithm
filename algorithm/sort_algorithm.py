def bubble_sort(li):
    """冒泡排序 最优O(n) 最坏O(n^2) 稳定"""
    for j in range(len(li) - 1, 0, -1):
        flag = False
        for i in range(j):
            if li[i] > li[i + 1]:
                li[i], li[i + 1] = li[i + 1], li[i]
                flag = True
        if not flag:
            break


def select_sort(li):
    """选择排序 最坏O(n^2) 不稳定"""
    for j in range(len(li)):
        mini = j
        for i in range(j + 1, len(li)):
            if li[i] < li[mini]:
                mini = i
        li[j], li[mini] = li[mini], li[j]


def insert_sort(li):
    """插入排序 最优O(n)  最坏O(n^2) 稳定"""
    for j in range(1, len(li)):
        for i in range(j, 0, -1):
            if li[i] < li[i - 1]:
                li[i], li[i - 1] = li[i - 1], li[i]
            else:
                break


def shell_sort(li, gap=None):
    """希尔排序 最优O(n^1.3) 最坏O(n^2) 不稳定"""
    n = len(li)
    if not gap:
        gap = n // 2
    while gap > 0:
        for j in range(gap, n):
            for i in range(j, gap - 1, -gap):
                if li[i] < li[i - gap]:
                    li[i], li[i - gap] = li[i - gap], li[i]
                else:
                    break
        gap //= 2


def quick_sort(li):
    """快速排序 最坏O(n^2) 最优O(nlogn) 不稳定"""
    return li if len(li) <= 1 else quick_sort([le for le in li[1:] if le <= li[0]]) + [li[0]] + quick_sort([gt for gt in li[1:] if gt > li[0]])


def merge_sort(li):
    """归并排序"""
    n = len(li)
    if n <= 1:
        return
    mid = n // 2
    left_li = merge_sort(li[:mid])
    right_li = merge_sort(li[mid:])
    left_pointer = right_pointer = 0
    result = []
    while left_pointer < len(left_li) and right_pointer < len(right_li):
        if left_li[left_pointer] < right_li[right_pointer]:
            result.append(left_li[left_pointer])
            left_pointer += 1
        else:
            result.append(right_li[right_pointer])
            right_pointer += 1
    result += left_li[left_pointer:]
    result += right_li[right_pointer:]


a = [54, 26, 93, 17, 77, 31, 44, 56, 20]
b = quick_sort(a)
print(a)
print(b)
