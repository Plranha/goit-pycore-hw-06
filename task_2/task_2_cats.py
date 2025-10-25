def get_cats_info(file_path):                                                   #Створюємо функцію тільки з одним параметром
    cats_list = []                                                              #Добавляємо переміну 
    try:
        with open(file_path,'r', encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) >=3:
                    cat_dict = {
                        'id': parts [0],
                        'name': parts [1],
                        'year':parts[2]
                    }
                    cats_list.append(cat_dict)
        return cats_list
    except Exception as e:
        print(f"Помилка {e}")
        

result = get_cats_info(r'task_2\cats.txt')
print(result)