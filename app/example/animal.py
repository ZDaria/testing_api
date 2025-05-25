

class Animal:
    def __init__(self):
        self._hunger_level: int = 50
        self.i_love_it: list = []
        self.voiсe: str = ""

    def speak(self):
        """возвращает звук животного"""
        return self.voiсe

    def feed(self, food: str):
        """возвращает, ест ли животное данную еду"""
        result = "Я это не ем!"
        if food in self.i_love_it:
            result = "Было вкусно!"
        return result

    def get_hunger_level(self):
        """_hunger_level — уровень голода (0–100),
        которое можно менять только через методы"""
        return self._hunger_level

    def eat(self, amount: int):
        self._hunger_level = min(100, self._hunger_level + amount)
        return self._hunger_level


class Lion(Animal):
    def __init__(self):
        super().__init__()
        self.voiсe = "Ррррр"
        self.i_love_it = ["мясо", "рыба", "курица"]


class Elephant(Animal):
    def __init__(self):
        super().__init__()
        self.voiсe = "Уууу"
        self.i_love_it = ["банан", "арбуз", "дыня"]


class Monkey(Animal):
    def __init__(self):
        super().__init__()
        self.voiсe = "Ууаааа"
        self.i_love_it = ["банан", "арбуз", "дыня"]


animals = [Lion(), Elephant(), Monkey()]
for animal in animals:
    print(animal.speak())
    print(animal.feed("банан"))

