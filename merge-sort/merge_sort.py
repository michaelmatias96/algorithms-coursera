def merge_sort(arr):
    if len(arr) == 1:
        return arr

    else:
        middle_index = len(arr) / 2
        left_half = arr[:middle_index]
        right_half = arr[middle_index:]

        merge_sort(left_half)
        merge_sort(right_half)

        return merge(left_half, right_half)


def merge(a, b):
    c = []

    while len(a) > 0 and len(b) > 0:
        if a[0] < b[0]:
            c.append(a.pop(0))

        else:
            c.append(b.pop(0))

    while len(a) > 0:
        c.append(a.pop(0))

    while len(b) > 0:
        c.append(b.pop(0))

    return c


if __name__ == '__main__':
    print(merge_sort([3, 4, 1, 2]))
