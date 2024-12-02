from datetime import datetime

def determine_quarter(date_str):
    """
    Функція визначає квартал року для заданої дати.
    Формат введення дати: 'YYYY-MM-DD' (рік-місяць-день).
    """
    try:
        
        date = datetime.strptime(date_str, '%Y-%m-%d')
        month = date.month

        
        if 1 <= month <= 3:
            return f"Дата {date_str} відноситься до 1-го кварталу."
        elif 4 <= month <= 6:
            return f"Дата {date_str} відноситься до 2-го кварталу."
        elif 7 <= month <= 9:
            return f"Дата {date_str} відноситься до 3-го кварталу."
        elif 10 <= month <= 12:
            return f"Дата {date_str} відноситься до 4-го кварталу."
    except ValueError:
        return "Невірний формат дати. Будь ласка, використовуйте формат 'YYYY-MM-DD'."


if __name__ == "__main__":
    print("Будь ласка, введіть дату у форматі 'YYYY-MM-DD' (рік-місяць-день).")
    input_date = input("Введіть дату: ")
    print(determine_quarter(input_date))
