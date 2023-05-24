import abc
from time import sleep, time


def time_record(function):
    def wrapper(*args, **kwargs):
        start_time = time()
        res = function(*args, **kwargs)
        end_time = time()
        return res, f'executed in -- {end_time - start_time} sec.'

    return wrapper


def record_decor(function):
    def wrapper(*args, **kwargs):
        res = function(*args, **kwargs)
        with open('reports/log_file.txt', 'a', encoding='utf-8') as file:
            file.write(f'Method {function.__name__} -- {res}\n')
        return res

    return wrapper


class Animal(abc.ABC):
    '''
    Abstract class determines the child-classes.
    '''
    def __init__(self, name: str, color: str, weight: int) -> None:
        self.name = name
        self.color = color
        self.weight = weight
        self._speed = lambda speed_factor: int(self.weight * speed_factor)

    @abc.abstractmethod
    def get_speed(self, speed_factor):
        pass

    @abc.abstractmethod
    def move(self):
        pass

    @abc.abstractmethod
    def bite(self):
        pass

    @abc.abstractmethod
    def important_info(self):
        pass


class Dog(Animal):
    '''
    Class creates dog-objects.
    '''
    def __init__(self, name, color, role_for_human='friend', weight=30, height=30) -> None:
        super().__init__(name, color, weight)
        self.role_for_human = role_for_human
        self.weight = weight
        self.height = height
    @time_record
    @record_decor
    def move(self):
        sleep(3)
        return f"The dog {self.name} moves at a speed {self.get_speed()}."

    def get_speed(self, speed_factor=0.8):
        return self._speed(speed_factor)

    def bite(self):
        return f"The dog {self.name} can bite in order to defend the owner."

    def reproduce(self, other):
        if isinstance(other, Dog):
            new_name = self.name + "-" + other.name
            new_color = self.color + "-" + other.color
            return Dog(new_name, new_color)
        else:
            raise Exception("Reproduce partner should be dog.")
    def important_info(self):
        return f'This is a dog. Its name is {self.name}. It is {self.color}. It is {self.role_for_human} for human.'


class Cat(Animal):
    '''
    Class creates cat-objects.
    '''
    def __init__(self, name: str, color: str, role_for_human='antistress', weight=5, character='lovely') -> None:
        super().__init__(name, color, weight=5)
        self.role_for_human = role_for_human
        self.weight = weight
        self.character = character

    def get_speed(self, speed_factor=5):
        return self._speed(speed_factor)

    @time_record
    @record_decor
    def move(self):
        sleep(1)
        return f"The cat {self.name} moves at a speed {self.get_speed()}."

    def bite(self):
        return f"The cat {self.name} bites gently in order to show love and confidence."

    def important_info(self):
        return f'This is a cat. Its name is {self.name}. It is {self.color}. It is {self.character}.'


class Horse(Animal):
    '''
    Class creates horse-objects.
    '''
    def __init__(self, name: str, color: str, role_for_human='riding', height=150) -> None:
        super().__init__(name, color, weight=500)
        self.role_for_human = role_for_human
        self.height = height

    def get_speed(self, speed_factor=0.18):
        return self._speed(speed_factor)

    @time_record
    @record_decor
    def move(self):
        sleep(2)
        return f"The horse {self.name} moves at a speed {self.get_speed()}."

    def bite(self):
        return f"The horse {self.name} bites during the game to show friendliness."

    def important_info(self):
        return f'This is a horse. Its name is {self.name}. It helps humans in {self.role_for_human}.'
