import json
import csv
import os


def update_country_language(filename="country.json"):
    with open(filename, "r", encoding="utf-8") as f:
        country = json.load(f)

    country["язык"] = "французский"

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(country, f, ensure_ascii=False, indent=2)


def add_intern_from_json(json_file="test_json", csv_file="employees_with_salary.csv"):
    with open(json_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    new_row = [
        data["Имя"],
        data["Возраст"],
        data["Город"],
        "Стажёр",
        50000
    ]

    headers = ["Имя", "Возраст", "Город", "Должность", "Зарплата"]
    file_exists = os.path.exists(csv_file)

    with open(csv_file, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)

        if not file_exists:
            writer.writerow(headers)

        writer.writerow(new_row)


def main():
    update_country_language()
    add_intern_from_json()


if __name__ == "__main__":
    main()
