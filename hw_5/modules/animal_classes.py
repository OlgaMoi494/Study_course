class Animal:
    def __init__(self, name: str, color: str, weight: int, description = "") -> None:
        self.name = name
        self.color = color
        self.weight = weight
        self.description = description

    
    def important_info(self):
        return f'This is an animal. Nobody knows what kind is it, but it\'s cute.\n \
Its name is {self.name}. Its weight is {self.weight} kg. Its color is {self.color}\n \
There is description: {self.description}'



class Dog(Animal):
    def __init__(self, name, color, role_for_human='friend', weight=50,  height=30) -> None:
        super().__init__(name, color, weight=50, description=None)
        self.role_for_human = role_for_human
        self.weight = weight
        self.height = height

    def important_info(self):
        return f'This is a dog. Its name is {self.name}. It is {self.color}. It is {self.role_for_human} for human.'


class Cat(Animal):
    def __init__(self, name: str, color: str, role_for_human='antistress', weight=5, character='lovely') -> None:
        super().__init__(name, color, weight=5)
        self.role_for_human = role_for_human
        self.weight = weight
        self.character = character

    def important_info(self):
        return f'This is a cat. Its name is {self.name}. It is {self.color}. It is {self.character}.'


class Horse(Animal):
    def __init__(self, name: str, color: str, role_for_human='riding', weight=500, height=150) -> None:
        super().__init__(name, color, weight=500)
        self.role_for_human = role_for_human
        self.weight = weight
        self.height = height
    
    def important_info(self):
        return f'This is a horse. Its name is {self.name}. It helps humans in {self.role_for_human}.'
    