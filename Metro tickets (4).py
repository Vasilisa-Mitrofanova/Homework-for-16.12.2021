import math

n = int(input("Введите количество поездок: "))
number_of_trips = [60, 20, 10, 5, 1]

for count in number_of_trips:
    if math.floor(n/count) > 0:
        print(f"Количество билетов на {count} поездок: {math.floor(n/count)}")
    n %= count
