def total_salary(file_path):  # Створив функцію
   
   total = 0  #Зробив загальну змінну 
   count = 0  #Змінна для ділення працівників
   try:                                                            #Обернув в Try Except якщо фал не знайдений або битий
       with open(file_path, 'r', encoding='utf-8') as file:        #Обрав метод відкриття, та параметри для  нього
          for line in file:                                        #Зробив цикл щоб пройтись по всьому файлу
              parts = line.strip().split(',')                      #Дай зрозуміти програмі після чого шукати зарплатню, 
              if len(parts) >=2:                                   #Роблю перевірку, щоб була мінімальна кількість привників(2) бо буде ділення
                 salart_str = parts[1]                             #Даємо зрозуміти з якого індексу понимаємо()
                 salart_int = int(salart_str)                      #Переводимо форм string in int
                 total += salart_int                               #Додаємо зарплатню до всього банку
                 count = count +1                                  #Рахуємо скільки прцівників було добавлено
              avarage = total / count if count > 0 else 0          #Рахуємо загальню зп та працівників з перевіркою
          return  total , avarage                                  #Повертаємо 2 аргументи
   except FileNotFoundError:
        print(f"Файл {file_path} не було знайдено")
        return None
   except Exception as e:
       print(f"Помилка: {e}")
       return None


total, average = total_salary(r'task_1\salary_info.txt')
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")