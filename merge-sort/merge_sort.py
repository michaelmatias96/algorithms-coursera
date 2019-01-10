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


def merge(arr_a, arr_b):
    merged_arr = []

    while len(arr_a) > 0 and len(arr_b) > 0:
        if arr_a[0] < arr_b[0]:
            merged_arr.append(arr_a.pop(0))

        else:
            merged_arr.append(arr_b.pop(0))

    while len(arr_a) > 0:
        merged_arr.append(arr_a.pop(0))

    while len(arr_b) > 0:
        merged_arr.append(arr_b.pop(0))

    return merged_arr


if __name__ == '__main__':
    print(merge_sort([3, 4, 1, 2]))
