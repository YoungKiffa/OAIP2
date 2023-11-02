def main():


    s = int(input('Зарплата за месяц: '))
    a = int(input('Количесво часов отработаных в выходные: '))
    print('Размер премии', s * 0.01 * a)


if __name__ == "__main__":
    main()