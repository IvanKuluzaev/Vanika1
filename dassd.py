from abc import ABC, abstractmethod

# Интерфейс стратегии
class BehaviorStrategy(ABC):
    @abstractmethod
    def act(self):
        pass

# Конкретная стратегия: мяукать
class MeowStrategy(BehaviorStrategy):
    def act(self):
        return "Meow!"

# Конкретная стратегия: лаять
class BarkStrategy(BehaviorStrategy):
    def act(self):
        return "Bark!"

# Конкретная стратегия: летать
class FlyStrategy(BehaviorStrategy):
    def act(self):
        return "I am flying!"

# Базовый класс животного
class Animal:
    def __init__(self, name, behavior: BehaviorStrategy):
        self.name = name
        self.behavior = behavior
    
    def perform_action(self):
        return self.behavior.act()
    
    def set_behavior(self, behavior: BehaviorStrategy):
        self.behavior = behavior

# Конкретное животное: кошка
class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, MeowStrategy())

# Конкретное животное: собака
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, BarkStrategy())

# Конкретное животное: птица
class Bird(Animal):
    def __init__(self, name):
        super().__init__(name, FlyStrategy())

# Пример использования
cat = Cat("Tom")
dog = Dog("Rex")
bird = Bird("Tweety")

print(f"{cat.name} says: {cat.perform_action()}")  # Tom says: Meow!
print(f"{dog.name} says: {dog.perform_action()}")  # Rex says: Bark!
print(f"{bird.name} says: {bird.perform_action()}")  # Tweety says: I am flying!

# Мы можем изменить поведение животного
cat.set_behavior(BarkStrategy())  # Кошка теперь может лаять
print(f"{cat.name} now says: {cat.perform_action()}")  # Tom now says: Bark!

