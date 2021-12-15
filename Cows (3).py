x = int(input("Сколько коров? "))
list1 = [2, 3, 4]
list2 = [5, 6, 7, 8, 9, 0]
list3 = [11, 12, 13, 14, 15, 16, 17, 18, 19]

if x not in list3 and x%10 == 1:
    print(f'На лугу пасется {x} корова.')
elif x in list3 or x%10 in list2:
    print(f'На лугу пасется {x} коров.')
elif x not in list3 and x%10 in list1:
    print(f'На л14угу пасется {x} коровы.')