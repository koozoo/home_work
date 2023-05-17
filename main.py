"TASK 1"

class Triangle:
    __slots__ = ['a', 'b', 'c']

    def __init__(self, a: int, b: int, c: int):
        self.a = a
        self.b = b
        self.c = c

    def start(self) -> str:
        if a + b <= c or a + c <= b or b + c <= a:
            msg = "Треугольника с такими сторонами не существует"
        else:
            if a == b == c:
                msg = "Треугольник - равносторонний"
            elif a == b or a == c or b == c:
                msg = "Треугольник - равнобедренный"
            else:
                msg = "Треугольник - разносторонний"

        return msg


a, b, c = int(input("введите длину отрезка А: ")), int(input("введите длину отрезка B: ")), int(
    input("введите длину отрезка C: "))

triangle = Triangle(a=a, b=b, c=c)
print(triangle.start())

"TASK 2"
num = int(input("Введите число: "))

msg = ""
MIN = 0
MAX = 100000

if num <= MIN or num > MAX:
    msg = "Неверное значение!"
else:
    prime = True
    for i in range(2, int(num / 2) + 1):
        if num % i == 0:
            prime = False
            break
    if prime:
        msg = "Число простое"
    else:
        msg = "Число составное"

print(msg)

"TASK 3"
from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
TRY_LIMIT = 10

num = randint(LOWER_LIMIT, UPPER_LIMIT)

count = 1
while count < TRY_LIMIT + 1:

    msg = ""

    player_num = int(input("Введите число: "))

    if player_num > num:
        msg = f"Число больше, осталось попыток -> {TRY_LIMIT - count}"
    elif player_num < num:
        msg = f"Число меньше, осталось попыток -> {TRY_LIMIT - count}"
    elif player_num == num:
        msg = "Вы угадали !"

    print(msg)
    count += 1

if count == 11:
    print("Вы проиграли =<")
