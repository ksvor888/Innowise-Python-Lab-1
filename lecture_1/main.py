from colorama import init, Fore, Back, Style
init()
print(f"{Fore.RED}{Back.YELLOW}Hello World!{Style.RESET_ALL}")
print(f"{Fore.GREEN}Hello World in Green!{Style.RESET_ALL}")
print(f"{Fore.BLUE}{Style.BRIGHT}Hello World in Bright Blue!{Style.RESET_ALL}")
print(f"{Fore.MAGENTA}{Back.CYAN}Hello World with Magenta text and Cyan background!{Style.RESET_ALL}")


#Lecture 2
def generate_profile (age):
    if 0<=age<=12:
        return "Child"
    elif 13<=age<=19:
        return "Teenager"
    else:
        return "Adult"

user_name=input ("Введите свое имя:")
birth_year_str = input("Введите год рождения: ")
birth_year = int(birth_year_str)
current_age = 2025 - birth_year
hobbies = []
while True:
    hobby = input("Введите любимое хобби или наберите «stop», чтобы завершить: ")
    if hobby.lower() == "stop":
        break
    hobbies.append(hobby)
life_stage = generate_profile(current_age)
user_profile = {
    "name": user_name,
    "age": current_age,
    "life_stage": life_stage,
    "hobbies": hobbies}
print("\nРезюме профиля:")
print(f"•Имя: {user_profile['name']}")
print(f"•Возраст: {user_profile['age']}")
print(f"• Этап жизни: {user_profile['life_stage']}")

if not user_profile["hobbies"]:
    print("• Вы не упомянули никаких хобби")
else:
    print(f"• Любимые хобби ({len(user_profile['hobbies'])}):")
    for hobby in user_profile["hobbies"]:
        print(f" {hobby}")

#Lecture 3

students = []

def calculate_average(grades):
    return sum(grades) / len(grades) if grades else "N/A"

def find_student(name):
    return next((s for s in students if s["name"].lower() == name.lower()), None)

while True:
    print("\nАнализатор оценок студентов")
    print("1. Добавить студента | 2. Добавить оценки | 3. Отчёт | 4. Лучший студент | 5. Выход")

    try:
        choice = int(input("Ваш выбор: "))
    except ValueError:
        print("Ошибка: введите число 1–5.")
        continue

    if choice == 1:  # Добавить студента
        name = input("Имя студента: ").strip()
        if not name:
            print("Имя не может быть пустым.")
            continue
        if find_student(name):
            print(f"Студент {name} уже есть.")
        else:
            students.append({"name": name, "grades": []})
            print(f"Студент {name} добавлен.")

    elif choice == 2:  # Добавить оценки
        name = input("Имя студента: ").strip()
        student = find_student(name)
        if not student:
            print(f"Студент {name} не найден.")
            continue
        print(f"Оценки для {name} (0–100), 'стоп' — завершить:")
        while True:
            g = input("Оценка: ").strip().lower()
            if g == "стоп":
                break
            try:
                grade = int(g)
                if 0 <= grade <= 100:
                    student["grades"].append(grade)
                    print(f"Добавлено: {grade}")
                else:
                    print("Оценка 0–100!")
            except ValueError:
                print("Число или 'стоп'!")

    elif choice == 3:  # Отчёт
        if not students:
            print("Нет студентов.")
            continue
        print("\nОтчёт:")
        averages = []
        for s in students:
            avg = calculate_average(s["grades"])
            print(f"{s['name']}: {avg}")
            if avg != "N/A":
                averages.append(avg)
        if averages:
            print(f"\nМакс: {max(averages)}, Мин: {min(averages)}, Среднее: {sum(averages)/len(averages):.1f}")
        else:
            print("У всех нет оценок.")

    elif choice == 4:  # Лучший студент
        if not students:
            print("Нет студентов.")
            continue
        with_grades = [s for s in students if s["grades"]]
        if not with_grades:
            print("Ни у кого нет оценок.")
            continue

        max_avg = 0
        best_student = None

        for student in students:
            avg = calculate_average(student["grades"])
            if avg > max_avg:
                max_avg = avg
                best_student = student

        print(f"Лучший студент: {best_student['name']} (средняя оценка: {max_avg})")

    elif choice == 5:
        print("До свидания!")
        break

    else:
        print("Ошибка: пожалуйста, выберите число от 1 до 5.")