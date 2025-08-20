import sys

def calculate_min_moves(nums, max_moves=20):
    """
    Рассчитывает минимальное количество ходов для приведения всех элементов массива к одному числу.
    Если количество ходов превышает max_moves, возвращает соответствующее сообщение.
    """
    # Сортируем массив и находим медиану
    nums.sort()
    median = nums[len(nums) // 2]

    # Считаем количество ходов
    moves = sum(abs(num - median) for num in nums)

    # Проверяем ограничение по количеству ходов
    if moves > max_moves:
        return f"{max_moves} ходов недостаточно для приведения всех элементов массива к одному числу."
    return moves

def main():
    # Проверяем количество аргументов командной строки
    if len(sys.argv) != 2:
        print("Usage: python script.py input_file")
        return

    input_file = sys.argv[1]

    try:
        # Считываем данные из файла
        with open(input_file, 'r') as f:
            nums = [int(line.strip()) for line in f]

        # Проверяем, что массив не пустой
        if not nums:
            print("Файл пустой или не содержит чисел.")
            return

        # Рассчитываем минимальное количество ходов
        result = calculate_min_moves(nums)
        print(result)

    except FileNotFoundError:
        print("Файл не найден.")
    except ValueError:
        print("Файл содержит некорректные данные.")

if __name__ == "__main__":
    main()
