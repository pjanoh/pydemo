def greet_msg(user: str) -> str:
    return f"Hello, {user}"

print("Вас приветствует программа!")
name = input("Введи своё имя: ")
print(greet_msg(name))