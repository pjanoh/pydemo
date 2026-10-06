def greet_msg(user: str) -> str:
    return f"Hello, {user}"

def farewell_msg(user: str) -> str:
    return f"Goodbye, {user}"

print("Вас приветствует программа!")
name = input("Введи своё ИМЯ: ")
print(greet_msg(name))
print(farewell_msg(name))
