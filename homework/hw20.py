from typing import Callable
import csv


def password_validator(min_length: int = 8, min_uppercase: int = 1, min_lowercase: int = 1, min_special_chars: int = 2):
    """Декоратор для проверки выполнения условий регистрации пароля(длинна, заглавные и строчные буквы и спец символы"""

    def decorator(func: Callable) -> Callable:
        def wrapper(username: str, password: str) -> None:
            bad_log_string = ' '

            if len(password) < min_length:
                bad_log_string += f"Пароль должен быть не менее {min_length} символов \n"
            if sum(1 for c in password if c.isupper()) < min_uppercase:
                bad_log_string += f"Пароль должен содержать не менее {min_uppercase} заглавных букв\n "
            if sum(1 for c in password if c.islower()) < min_lowercase:
                bad_log_string += f"Пароль должен содержать не менее {min_lowercase} строчных букв\n"
            if sum(1 for c in password if not c.isalnum()) < min_special_chars:
                bad_log_string += f"Пароль должен содержать не менее {min_special_chars} спец символов\n"

            if bad_log_string:
                raise ValueError(bad_log_string)

            func(username, password)

        return wrapper

    return decorator


def username_validator() -> Callable:
    """Декоратор для проверки отсутствия пробелов в никнейме"""

    def decorator(func: Callable) -> Callable:
        def wrapper(username: str, password: str) -> None:
            if ' ' in username:
                raise ValueError("Никнейм не может содержать пробелов")
            func(username, password)

        return wrapper

    return decorator


@password_validator(min_length=10, min_uppercase=2, min_lowercase=2, min_special_chars=2)
@username_validator()
def register_user(username: str, password: str) -> None:
    """ Функция для регистрации нового пользователя
    """
    with open('users.csv', 'a', newline=' ') as file:
        writer = csv.writer(file)
        writer.writerow([username, password])


try:
    register_user("IgorOsnovin", "IgoR1997!!")
    print("Регистрация прошла успешно")
except ValueError as e:
    print(f'Ошибка {e}')

# УЖе не знаю где исправить код чтобы не выдавал ошибку(((