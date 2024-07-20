search_list = [1, 3, 4, 5, 7, 8, 9, 10, 13, 15, 18, 21]
n = len(search_list)
left = 0
right = n - 1
target = 18

while left <= right:
    mid = (left + right) // 2
    if search_list[mid] == target:
        print(f'Element is at index {mid}')
        break
    elif search_list[mid] > target:
        right = mid - 1
    else:
        left = mid + 1
else:
    print('Element not found')
