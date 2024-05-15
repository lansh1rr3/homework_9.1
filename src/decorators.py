from datetime import datetime
from typing import Any, Callable, Optional, Union


def log(filename: Optional[str] = None) -> Callable:
    """
    Декорирующая функция.
    """

    def decorator(func: Callable) -> Callable:
        """
        Обернутая функция.
        """

        def wrapper(*args: Any, **kwargs: Any) -> Union[str, Any]:
            """
            Возвращаемое значение декорируемой функции.
            """
            start = datetime.now()
            try:
                result = func(*args, *kwargs)
                status = "ok"
            except Exception as e:
                result = f"error: {e.__class__.__name__}"
                status = "error"
            end = datetime.now()
            log_message = f"{start} {func.__name__} {status} ({end - start}). Inputs: {args}, {kwargs}"
            print(log_message) if not filename else open(filename, "a").write(log_message + "\n")
            if status == "error":
                raise
            return result

        return wrapper

    return decorator


@log(filename="mylog.txt")
def my_function(x: int, y: int) -> int:
    """
    Пример функции, которая складывает два числа.
    """
    return x + y


my_function(1, 2)
