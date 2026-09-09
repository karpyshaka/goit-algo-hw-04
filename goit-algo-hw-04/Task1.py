
def total_salary(path):

    total = 0
    emp = 0

    try:
        with open(path, "r", encoding="utf-8") as fh:
            for line in fh:
                data = line.split(",")
                salary = data[1]
                total += int(salary)
                emp += 1
            

    except FileNotFoundError:
        print(f"За шляхом {path} Файл не знайдено, перевірте, чи правильно вказано шлях.")
        return None, None

    if emp == 0:
        print(f"За шляхом {path} Файл порожній.")
        return None, None

    avg_salary = total / emp

    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {avg_salary}")
    return total, avg_salary

total_salary("goit_hw/goit-algo-hw-04/task1.txt")