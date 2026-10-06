def greet_msg(user: str) -> str:
    return f"Hello, {user}"

name = input("Введи своё имя: ")
print(greet_msg(name))