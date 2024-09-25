import threading
from time import sleep
from random import randint


class Bank(threading.Thread):
    def __init__(self):
        super().__init__()
        self.balance = 0
        self.lock = threading.Lock()
        self.trans_up = 100
        self.trans_down = 100

    def deposit(self):
        while self.trans_up > 0:
            cash = randint(50, 500)
            self.balance += cash
            self.trans_up -= 1
            if self.balance >= 500 and self.lock.locked():    # проверка денег на балансе для открытия счета
                self.lock.release()
            print(f"Пополнение: {cash}. Баланс: {self.balance}.\n")
        sleep(0.01)

    def take(self):
        while self.trans_down > 0:
            cash = randint(50, 500)
            print(f"Запрос на {cash}")
            self.trans_down -= 1
            if self.lock.locked():    # Данное условие нужно, чтобы программа продолжила работать при закрытом счете
                print("Карта заблокирована, пополните баланс до 500\n")
            else:
                if cash <= self.balance:    # проверка денег на балансе для снятия
                    self.balance -= cash
                    print(f"Снятие:{cash}. Баланс: {self.balance}.\n")
                else:
                    print("Запрос отклонен, недостаточно средств.\n")
                    self.lock.acquire()

        sleep(0.01)


bk = Bank()
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f"Итоговый баланс: {bk.balance}")
