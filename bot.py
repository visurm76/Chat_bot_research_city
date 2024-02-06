import random
from users import User

new_users = []
question = int(input("Введите ваше действие: 1- регистрация пользователя; 2- диалог: "))
def registration_user():
    user_name = input("Введите Ваше имя: ").title()
    user_age = int(input("Введите Ваш возраст: "))
    user_email = input("Введите Ваш e-mail: ")
    user_new = User(user_name, user_age, user_email)
    return new_users.append(user_new.greet())

if question == 1:
    registration_user()
else:
    user_name = input("Введите Ваше имя: ").title()
    if user_name not in new_users:
        print("Ваше имя отсутствуют в списке собеседников")
        print("Пройдите регистрацию")
        registration_user()
    else:
        print("Вы зарегистрированы")

# Задаем возможные ответы бота
responses = {
    "привет": "Привет, как дела?",
    "что делаешь?": "Отвечаю на твои вопросы :)",
    "какой твой любимый цвет?": "Мой любимый цвет - синий.",
    "спасибо": "Пожалуйста!",
    "пока": "До свидания!",
}
"""
# Функция для обработки вопросов пользователя
def get_response(user_message):
    user_message = user_message.lower() # Приводим сообщение к нижнему регистру
    if user_message in responses:
        return responses[user_message]
    else:
        return "Извини, я не понимаю. Попробуй другой вопрос."

# Основной цикл чат бота
while True:
    user_input = input("Вы: ")
    response = get_response(user_input)
    print("Бот:", response)
"""
