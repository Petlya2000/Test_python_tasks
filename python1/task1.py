import sys

def circular_path(n, m):
    """
    Вычисляет путь для кругового массива длины n с интервалом m.
    """
    path = []
    current_index = 0  # Начинаем с первого элемента (индекс 0)

    while True:
        # Добавляем текущий элемент в путь
        path.append(current_index + 1)  # Индексы начинаются с 0, поэтому +1

        # Вычисляем следующий индекс
        current_index = (current_index + m) % n

        # Если вернулись к началу, завершаем цикл
        if current_index == 0:
            break

    return path

def main():
    # Проверяем количество аргументов командной строки
    if len(sys.argv) != 5:
        print("Usage: python script.py n1 m1 n2 m2")
        return

    # Считываем параметры для двух массивов
    n1, m1, n2, m2 = map(int, sys.argv[1:])

    # Вычисляем пути для двух массивов
    path1 = circular_path(n1, m1)
    path2 = circular_path(n2, m2)

    # Объединяем пути и выводим результат
    result = ''.join(map(str, path1 + path2))
    print(result)

if __name__ == "__main__":
    main()
