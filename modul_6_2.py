class Vehicle:
    __COLOR_VARIANTS = ["red", "blue", "black", "white", "green"] # текущие цвета
    def __init__(self, owner:str, model:str,color:str, engine_power:int):
        self.owner = owner #
        self.__model = model #
        self.__color = color
        self.__engine_power = engine_power #

    def get_model(self):
        return f'Модель: {self.model}'
    def get_horse_power(self):
        return f'Мощность двигателя: {self.engine_power}'
    def get_color(self):
        return f'Цвет: {self.color}'
    def print_info(self):
        print(f'{self.get_model()} \n{self.get_horse_power()} \n{self.get_color()} \nВладелец: {self.owner}')
    def set_color(self, new_color:str):
        self.new_color = new_color
        if self.new_color.lower() in Vehicle.__COLOR_VARIANTS:
            self.color = self.new_color
        else:
            print(f"Нельзя сменить на цвет {self.new_color}")

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()

