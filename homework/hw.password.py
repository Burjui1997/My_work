from typing import Callable

def password_checker(func: Callable[[str], str]) -> Callable[[str], str]:
    def wrapper(password: str) -> str:
        if len(password) >= 8 and any(char.isdigit() for char in password) \
                and any(char.isupper() for char in password) and any(char.islower() for char in password) \
                and any(char in "!@#$%^&*()_+" for char in password):
            return func(password)
        else:
            return "Ошибка: сложность пароля не соответствует требованиям."
    return wrapper

@password_checker
def register_user(password: str) -> str:
    return "Успешная регистрация."

print(register_user("Tesla123!"))
print(register_user("23121"))
print(register_user("tesla323"))
print(register_user("Как сложно учить программирование,Господи помоги123!"))