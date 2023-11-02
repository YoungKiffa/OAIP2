def main():


    s = int(input('Напишите количество купюр: '))
    sa = s // 1000
    s = s % 1000
    se = s // 100
    s = s % 100
    sf = s // 10
    s = s % 10
    print(s)
    print(sf)
    print(se)
    print(sa)


if __name__ == "__main__":
    main()