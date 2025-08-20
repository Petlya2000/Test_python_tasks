import sys

def check_point_position(center, radii, point):
    """
    Проверяет положение точки относительно эллипса.
    Возвращает:
    0 - точка лежит на эллипсе,
    1 - точка внутри эллипса,
    2 - точка снаружи эллипса.
    """
    h, k = center  # Центр эллипса
    a, b = radii   # Радиусы эллипса
    x, y = point   # Координаты точки

    # Уравнение эллипса: ((x - h)^2 / a^2) + ((y - k)^2 / b^2)
    value = ((x - h) ** 2) / (a ** 2) + ((y - k) ** 2) / (b ** 2)

    if abs(value - 1) < 1e-9:  # Учитываем погрешность для чисел с плавающей точкой
        return 0  # Точка лежит на эллипсе
    elif value < 1:
        return 1  # Точка внутри эллипса
    else:
        return 2  # Точка снаружи эллипса

def main():
    # Проверяем количество аргументов командной строки
    if len(sys.argv) != 3:
        print("Usage: python script.py ellipse_file points_file")
        return

    ellipse_file = sys.argv[1]
    points_file = sys.argv[2]

    try:
        # Считываем данные из файла с эллипсом
        with open(ellipse_file, 'r') as f:
            center = tuple(map(float, f.readline().strip().split()))  # Координаты центра
            radii = tuple(map(float, f.readline().strip().split()))   # Радиусы эллипса

        # Считываем данные из файла с точками
        with open(points_file, 'r') as f:
            points = [tuple(map(float, line.strip().split())) for line in f]

        # Проверяем каждую точку и выводим результат
        for point in points:
            result = check_point_position(center, radii, point)
            print(result)

    except FileNotFoundError:
        print("One of the input files was not found.")
    except ValueError:
        print("Invalid data format in input files.")

if __name__ == "__main__":
    main()
