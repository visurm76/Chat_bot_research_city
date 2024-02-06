class User:
    def __init__(self, username, age, email):
        self.username = username
        self.age = age
        self.email = email

    def greet(self):
        #return f"Привет, я {self.username}! Мне {self.age} лет. Мой email: {self.email}"
        lst_users = {self.username: [self.age, self.email]}
        return lst_users

# Пример создания объекта пользователя
#user1 = User("Alice", 25, "alice@example.com")
#print(user1.greet())