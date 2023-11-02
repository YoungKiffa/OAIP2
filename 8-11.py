def main():


    # 8.1 ZAdanie
    cs = [0]
    print(cs)

    # 8.2
    sys = [0, 1]
    sys.append(5)
    print(sys)

    # 8.3
    sws = [1, 1, 2, 3, 4, 6, 7, 8, 4, 2, 0]
    sws.remove(1)
    print(sws)

    # 8.4
    print(sws[1:9])

    # 8.5
    sws.reverse()
    print(sws[::-1])

    # 8.6 and 8.7
    ff = [[1, 2, 3], [[1, 8, 0, 7], 7, 9]]
    print(ff[0][2:])
    print(ff[1][0][1])

    # 8.8
    m = [1, 2, 3, 4, 5]
    m.clear()
    print(m)

    # 9.1 ZAdanie
    a = ()
    print(a)

    #9.2
    sqs = (52, "Главная задача успеть", 6, "успел")
    print(sqs)

    #10.1 ZAdanie
    cat = {}
    print(cat)

    #10.2
    cat2 = {"1,2,3"}
    print(cat2)

    #10.3
    cat3 = {'a', 'b', 'c'}
    cat3.add('d')
    print(cat3)

    #10.4
    cat4 = {1, 3, 6, 2, 8}
    cat41 = {1, 7, 9, 0, 6}
    print(cat4.intersection(cat41))

    #10.5 Перечисление
    cat5 = {1, 2, 3}
    cat51 = {4, 5, 6}
    print(cat5.union(cat51))

    #10.6 Объединение
    cat6 = {9, 4, 0, 2, 1, 7}
    cat61 = {1, 4, 3, 5, 8, 9}
    print(cat6.difference(cat61))

    #10.7 Разность
    cat7 = {1, 2, 3, 4}
    cat71= {6, 8, 4, 2}
    print(cat7.symmetric_difference(cat71))

    #11.1 ZAdanie
    info_dict = {}
    my_dict = dict()

    #11.2
    car = {'Марка': 'Subaru', 'Модель': 'Impreza WRX STI', 'Год': '2003', 'Цвет': 'Красный', 'Пробег': '50142 км'}
    print(car)

    #11.3
    pe_dict = {'Профессия': 'Водитель', 'Имя': 'Райн'}
    pe_dict['Фамилия'] = 'Гослинг'
    print(pe_dict)

    #11.4
    xax_dict = {'Жанр': 'Хоррор', 'Рейтинг': 5.5, 'Название': 'Мишк Фреддэ'}
    del xax_dict['Рейтинг']
    print(xax_dict)

    #11.5
    sas_dict = {'Профессия': 'Водитель', 'Имя': 'Райн'}
    sas_dict['Имя'] = 'Доменик'
    print(sas_dict)


if __name__ == "__main__":
    main()