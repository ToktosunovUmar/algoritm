def selection_sort(numbers):
    n = len(numbers)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if numbers[j] > numbers[min_index]:
                min_index = j
        numbers[j], numbers[min_index] = numbers[min_index],numbers[j]


numbers = [64, 25, 12, 22, 11]
selection_sort(numbers)
print("Отсортированный список:", numbers)
