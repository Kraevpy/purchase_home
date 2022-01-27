from purchase import *

if __name__ == '__main__':
    Human.default_info()

    Ignat = Human('Ignat', 20)

    small_house = SmallHouse(7900)

    Ignat.buy_house(small_house, 5)

    Ignat.earn_money(2500)
    Ignat.buy_house(small_house, 5)

    Ignat.earn_money(15000)
    Ignat.buy_house(small_house, 5)
    Ignat.info()
