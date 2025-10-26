import sys
from pathlib import Path
from colorama import Fore, Style, init

init()

def visualize_directory(path, level=0, max_depth=2):
    try:
        directory = Path(path)
        
        if not directory.exists() or not directory.is_dir():
            print(f"{Fore.RED}Помилка: Невірний шлях до директорії{Style.RESET_ALL}")
            return

        items = sorted(directory.iterdir(), key=lambda x: (x.is_file(), x.name.lower()))
        
        for item in items:
            indent = "    " * level
            if item.is_dir():
                print(f"{indent}{Fore.BLUE}{item.name}/{Style.RESET_ALL}")
                if level < max_depth - 1:  # Динамічна глибина
                    visualize_directory(item, level + 1, max_depth)
            else:
                print(f"{indent}{Fore.GREEN}{item.name}{Style.RESET_ALL}")
                
    except PermissionError:
        print(f"{'    ' * level}{Fore.RED}[Доступ заборонено]{Style.RESET_ALL}")

if __name__ == "__main__":
    if len(sys.argv) not in [2, 3]:
        print(f"{Fore.YELLOW}Використання: {sys.argv[0]} <шлях до директорії> [глибина]{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Приклад: {sys.argv[0]} . 3{Style.RESET_ALL}")
        sys.exit(1)
    
    path = sys.argv[1]
    max_depth = int(sys.argv[2]) if len(sys.argv) == 3 else 2
    
    print(f"{Fore.CYAN}Структура директорії (глибина: {max_depth}):{Style.RESET_ALL}")
    visualize_directory(path, max_depth=max_depth)

#Виклик працював за -> python task_3/task_3.py "Шлях до файлу"