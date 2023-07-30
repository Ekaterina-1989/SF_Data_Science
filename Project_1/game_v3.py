"""Игра: Угадай число.
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np
import random

def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    
    count = 0
    start = 1  # Присваиваем значение, которое соответствует нижней границе диапазона поиска
    stop = 101  # Присваиваем значение, которое соответствует верхней границе диапазона поиска

    while True:
        average_number = (start + stop)//2
        count += 1
        if average_number == number:
            break  # Выход из цикла, если угадали
        elif number > average_number:
            start = average_number  # Перезаписываем переменную start
        else:
            stop = average_number # Перезаписываем переменную stop

    return(count)





def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    
    count_ls = [] # Список для сохранения количества попыток
    np.random.seed(1)  # Фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # Загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))
    score = int(np.mean(count_ls))

    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток")

    return(score)


    # RUN
if __name__ == "__main__":
    score_game(random_predict)