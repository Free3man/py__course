import math


def sales_prediction():
    summary = float(input("Проєктована сума: "))
    print(1.19 * summary)


def yard_to_meter():
    length = float(input("Довжина у ярдах: "))
    print(0.914 * length)


def cashier():
    cash = 0
    for i in range(5):
        price = round(float(input(f"Товар {i}: ")), 2)
        cash += price
    pdv = round(cash * 0.14, 2)
    end_cash = cash + pdv
    print(f'Сума кошика: {cash}')
    print(f'ПДВ: {pdv}')
    print(f'Сума до оплати з ПДВ: {end_cash}')


def odometer():
    v0 = float(input("Введіть початкову швидкість: "))
    a = float(input("Введіть прискорення: "))
    t1 = float(input("Введіть перший проміжок часу: "))
    t2 = float(input("Введіть другий проміжок часу: "))
    s1 = v0 * t1 + ((a * t1 ** 2) / 2)
    v1 = v0 + a * t1
    s2 = v1 * t2
    print(f"S1: {s1}; S2: {s2}")


def payment_instalments():
    start_sum = int(input("Введіть суму покупки: "))
    n = int(input("Введіть кількість платежів: "))
    full_sum = round(start_sum * 1.05, 2)
    payment = full_sum / n
    print(f"Загальна сума: {full_sum}")
    print(f"Сума кожного платежу: {payment}")


def miles_per_gallon():
    miles = int(input("Кількість пройдених миль: "))
    gallons = int(input("Використана кількість бензину: "))
    mpg = round(miles / gallons, 3)
    print(f"MPG: {mpg}")


def cookie():
    sugar = 1.5 / 48
    butter = 1 / 48
    flour = 2.75 / 48
    n = int(input("Кількість печива: "))
    print(f"{n * sugar} склянок цукру")
    print(f"{n * butter} склянок вершового масла")
    print(f"{n * flour} склянок борошна")


def vineyard():
    r = float(input("Довжина ряду, у футах: "))
    e = float(input("Довжина, у футах, що використовується опорою: "))
    s = float(input("Відстань між кущами, у футах: "))
    v = (r - 2 * e) / s
    print(f"Кількість виноградних кущів, що помістяться в ряд: {v}")


def compound_interest():
    p = float(input("Основна сума, яка спочатку була внесена на рахунок: "))
    r = float(input("Річна процентна ставка: "))
    n = int(input("Кількість разів на рік, коли відсотки виплачуються: "))
    t = int(input("Вказана кількість років: "))
    a = pow(p * (1 + r / n), n*t)
    print(f"Сума грошей на рахунку через зазначену кількість років: {a}")


if __name__ == "__main__":
    eval(input() + "()")