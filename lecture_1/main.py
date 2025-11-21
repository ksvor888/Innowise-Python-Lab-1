from colorama import init, Fore, Back, Style
init()
print(f"{Fore.RED}{Back.YELLOW}Hello World!{Style.RESET_ALL}")
print(f"{Fore.GREEN}Hello World in Green!{Style.RESET_ALL}")
print(f"{Fore.BLUE}{Style.BRIGHT}Hello World in Bright Blue!{Style.RESET_ALL}")
print(f"{Fore.MAGENTA}{Back.CYAN}Hello World with Magenta text and Cyan background!{Style.RESET_ALL}")

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