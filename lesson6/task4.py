"""
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение
о превышении скорости.
"""


class Car:

    def __init__(self, name, speed, color, is_police=False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        return f'Автомобиль {self.name} двинулась.'

    def stop(self):
        return f'\nАвтомобиль {self.name} остановилась.'

    def turn(self, direction):
        return f'\nАвтомобиль {self.name} повернула в {direction}'

    def show_speed(self):
        return f'\nСкорость Автомобиля {self.speed}'


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'\nСкорость {self.speed}км/ч, выше чем позволяет! '
        else:
            return f'\nСкорость {self.name} нормально!'


town = TownCar('AudiA4', 70, False)
print('1:\n' + town.go(), town.show_speed(), town.turn('лево'), town.turn('право'), town.stop())


class SportCar(Car):
    def show_speed(self):
        if self.speed == 50:
            return


sport = SportCar('AudiA6', 50, False)
print('2:\n' + sport.go(), sport.show_speed(), sport.turn('лево'), sport.stop())


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'\nСкорость выше, чем позволяет! {self.speed}'
        else:
            return f'\nСкорость {self.name} нормально!'


work = WorkCar('AudiA8', 30, False)
print('3:\n' + work.go(), work.show_speed(), work.turn('право'), work.stop())


class PoliceCar(Car):
    def show_speed(self):
        if self.speed == 50:
            return


police = PoliceCar('AudiRs', 170, False)
print('4:\n' + police.go(), police.show_speed(), police.turn('право'), police.stop())

