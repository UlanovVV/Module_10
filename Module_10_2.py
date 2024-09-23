import threading
import time

class Knight(threading.Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.enemies = 123
        self.days = 0

    def run(self):
        print(f"{self.name}, на нас напали!")
        while self.enemies > 0:
            self.enemies -= self.power
            self.days += 1
            time.sleep(1) # Задержка на 1 секунду
            if self.enemies <= 0:
                self.enemies = 0 #Приравниваем значение, чтобы количество воинов небыло отрицательным
                print(f"{self.name} сражается {self.days} день(дня)..., осталось {self.enemies} воинов.\n", end=" ")
                print(f"{self.name} одержал победу спустя {self.days} дней(дня)! \n", end=" ")
            else:
                print(f"{self.name} сражается {self.days} день(дня)..., осталось {self.enemies} воинов.\n", end=" ")


# Создание и запуск рыцарей
knight1 = Knight("Ланцелот", 10)
knight2 = Knight("Галахад", 15)
knight3 = Knight("Персиваль", 20)

knight1.start()
knight2.start()
knight3.start()

knight1.join()
knight2.join()
knight3.join()

print("Все битвы закончелись!")
