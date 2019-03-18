from turtle import *


def koch(order, size):
    if order == 0:
        forward(size)
        
    else:
        koch(order-1, size/3)
        left(60)
        koch(order-1, size/3)
        right(120)
        koch(order-1, size/3)
        left(60)
        koch(order-1, size/3)


def koch_main():
    up()
    speed(7)
    goto(-100, 0)
    down()
    n = int(input('Глубина рекурсии:'))
    a = int(input('Длина стороны:'))
    koch(n, a)
    mainloop()


def snowflake(n, k):
    for _ in range(3):
        if n == 0:
            forward(k)
            right(120)
        else:
            koch(n - 1, k)
            right(120)


def snowflake_main():
    up()
    speed(7)
    goto(-100, 0)
    down()
    n = int(input('Глубина рекурсии:'))
    a = int(input('Длина стороны:'))
    snowflake(n, a)
    mainloop()


def tree(n, d):
    if n == 0:
        return
    else:
        forward(d)
        right(30)
        tree(n - 1, d * 0.7)
        left(60)
        tree(n - 1, d * 0.7)
        right(30)
        backward(d)


def tree_main():
    up()
    speed(7)
    left(90)
    goto(0, 0)
    down()
    n = int(input('Глубина рекурсии:'))
    a = int(input('Длина стороны:'))
    tree(n, a)
    mainloop()


def mink(n, d):
    speed(7)
    if n == 0:
        forward(d)
    else:
        mink(n - 1, d)
        left(90)
        mink(n - 1, d)
        right(90)
        mink(n - 1, d)
        right(90)
        mink(n - 1, d)
        mink(n - 1, d)
        left(90)
        mink(n - 1, d)
        left(90)
        mink(n - 1, d)
        right(90)
        mink(n - 1, d)


def mink_main():
    up()
    speed(7)
    goto(-330, 0)
    down()
    n = int(input('Глубина рекурсии:'))
    if n <= 1:
        a = 150
    else:
        a = 150 / (2.5 * n ** 1.5)
    mink(n, a)
    mainloop()


def led_1(order, size):
    if order == 0:
        forward(size)
    else:
        led_1(order-1, size)
        left(90)
        led_1(order-1, size/2)
        right(180)
        led_1(order-1, size/2)
        left(90)
        led_1(order-1, size)


def led_1_main():
    up()
    goto(-280,-100)
    down()
    n = int(input('Глубина рекурсии:'))
    a = int(input('Длина стороны:'))
    led_1(n, a)


def led_2(order, size):
    if order == 0:
        forward(size)
    else:
        led_2(order-1, size)
        left(120)
        led_2(order-1, size/2)
        right(180)
        led_2(order-1, size/2)
        left(120)
        led_2(order - 1, size / 2)
        right(180)
        led_2(order - 1, size / 2)
        left(120)
        led_2(order - 1, size)


def led_2_main():
    up()
    goto(-280,-100)
    down()
    n = int(input('Глубина рекурсии:'))
    a = int(input('Длина стороны:'))
    led_2(n, a)
    mainloop()


def levi(order, size):
    if order == 0:
        forward(size)
    else:
        left(45)
        levi(order-1, size)
        right(90)
        levi(order-1, size)
        left(45)


def levi_main():
    up()
    goto(-100,0)
    down()
    n = int(input('Глубина рекурсии:'))
    a = int(input('Длина стороны:'))
    levi(n, a)
    mainloop()


def dragon_1(order, size):
    if order == 0:
        forward(size)
    else:
        left(45)
        dragon_1(order-1, size)
        right(90)
        dragon_2(order-1, size)
        right(45)


def dragon_2(order, size):
    if order == 0:
        forward(size)
    else:
        left(45)
        dragon_1(order-1, size)
        left(90)
        dragon_2(order-1, size)
        right(45)


def dragon_main():
    up()
    goto(0,0)
    down()
    n = int(input('Глубина рекурсии:'))
    a = int(input('Длина стороны:'))
    dragon_1(n, a)
    mainloop()


def main():
    print('Построение фракталов:')
    print('1.Квадрат \n2.Двоичное дерево \n3.Кривая Коха \n4.Снежинка Коха \n'
          '5.Кривая Минковского \n6."Ледяной" фрактал 1 \n7."Ледяной" фрактал 2 \n'
          '8.Кривая Леви \n9.Дракон Хартера-Хейтуэя')
    fractal = int(input('Построить фрактал: '))
    if fractal == 2:
        tree_main()
    if fractal == 3:
        koch_main()
    if fractal == 4:
        snowflake_main()
    if fractal == 5:
        mink_main()
    if fractal == 2:
        tree_main()
    if fractal == 6:
        led_1_main()
    if fractal == 7:
        led_2_main()
    if fractal == 8:
        levi_main()
    if fractal == 9:
        dragon_main()

if __name__ == '__main__':
    main()


