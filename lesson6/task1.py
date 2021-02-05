"""
Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет)
и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы:
красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке (красный,
желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
"""
from time import sleep
from tkinter import *

class TrafficLight(Tk):

    def __init__(self):
        self.state = 0
        super().__init__()
        self.title('Светофор')
        self.canvas = c = Canvas(self, width=70, height=190, bg="black")
        self.r = c.create_oval(10, 10, 60, 60, fill="#ff0000")
        self.y = c.create_oval(10, 70, 60, 120, fill="#808000")
        self.g = c.create_oval(10, 130, 60, 180, fill="#008000")
        c.pack()
        self.update()
        self.after(3000, self.upd)

    def upd(self):
        if self.state == 0:
            self.state = 1
            self.canvas.itemconfigure(self.r, fill='#800000')
            self.canvas.itemconfigure(self.y, fill='#ffff00')
            self.after(500, self.upd)
        elif self.state == 1:
            self.state = 2
            self.canvas.itemconfigure(self.y, fill='#808000')
            self.canvas.itemconfigure(self.g, fill='#00ff00')
            self.after(2000, self.upd)
        elif self.state == 2:
            self.state = 3
            self.canvas.itemconfigure(self.g, fill='#008000')
            self.canvas.itemconfigure(self.y, fill='#ffff00')
            self.after(750, self.upd)
        else:
            self.state = 0
            self.canvas.itemconfigure(self.r, fill='#ff0000')
            self.canvas.itemconfigure(self.y, fill='#808000')
            self.after(3000, self.upd)


root = TrafficLight()
root.mainloop()

# второй вариант
class TrafficLight:
    __color = ['Красный', 'Желтый', 'Зеленый']

    def running(self):
        i = 0
        while i != 3:
            print(TrafficLight.__color[i])
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(2)
            elif i == 2:
                sleep(5)
            i += 1


t = TrafficLight()
t.running()
