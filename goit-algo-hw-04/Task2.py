
def get_cats_info(path):
    cats = []

    try:
        with open(path, "r", encoding="utf-8") as fh:
            for line in fh:
                data = line.strip().split(",")
                cat_id = data[0]
                name = data[1]
                age = data[2]
                cat = {
                    "id":cat_id,
                    "name":name,
                    "age":age
                }
                cats.append(cat)
        
    except FileNotFoundError:
        print(f"За шляхом {path} Файл не знайдено, перевірте, чи правильно вказано шлях.")
        return []
    if len(cats) == 0:
        print(f"За шляхом {path} Файл порожній.")
        return []

    print(cats)
    return cats

get_cats_info("goit_hw/goit-algo-hw-04/task2.txt")