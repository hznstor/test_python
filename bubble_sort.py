def bubble_sort(arr):
    n = len(arr)
    # Проходим по всем элементам массива
    for i in range(n):
        # Флаг для оптимизации: если на проходе не было обменов, массив уже отсортирован
        swapped = False
        # Последние i элементов уже на месте после каждой итерации
        for j in range(0, n - i - 1):
            # Сравниваем соседние элементы
            if arr[j] > arr[j + 1]:
                # Меняем элементы местами
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # Если не было обменов — сортировка завершена
        if not swapped:
            break
    return arr

# Пример использования
if __name__ == "__main__":
    data = [10, 7, 8, 3, 1, 7, 6, 5, 4, 9, 6, 8, 1]
    print("Исходный массив:", data)
    sorted_data = bubble_sort(data)
    print("Отсортированный массив:", sorted_data)

