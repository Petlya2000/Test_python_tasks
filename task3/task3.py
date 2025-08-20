import json
import sys

def fill_values(tests, values_dict):
    """
    Рекурсивно заполняет поле 'value' в структуре tests на основе values_dict.
    """
    for test in tests:
        # Если id теста есть в values_dict, заполняем поле value
        if test["id"] in values_dict:
            test["value"] = values_dict[test["id"]]
        
        # Если есть вложенные тесты, рекурсивно обрабатываем их
        if "values" in test:
            fill_values(test["values"], values_dict)

def main():
    # Проверяем количество аргументов командной строки
    if len(sys.argv) != 4:
        print("Usage: python script.py tests.json values.json report.json")
        return

    tests_file = sys.argv[1]
    values_file = sys.argv[2]
    report_file = sys.argv[3]

    try:
        # Считываем данные из tests.json
        with open(tests_file, 'r') as f:
            tests_data = json.load(f)

        # Считываем данные из values.json
        with open(values_file, 'r') as f:
            values_data = json.load(f)

        # Преобразуем values.json в словарь для быстрого доступа
        values_dict = {item["id"]: item["value"] for item in values_data["values"]}

        # Заполняем поле 'value' в структуре tests
        fill_values(tests_data["tests"], values_dict)

        # Записываем результат в report.json
        with open(report_file, 'w') as f:
            json.dump(tests_data, f, indent=2)

        print(f"Report successfully written to {report_file}")

    except FileNotFoundError as e:
        print(f"File not found: {e.filename}")
    except json.JSONDecodeError:
        print("Error decoding JSON. Please check the input files.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
