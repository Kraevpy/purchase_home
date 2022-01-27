class Human:
    default_name = 'name missing'
    default_age = 0

    def __init__(self, name=default_name, age=default_age):
        self.age = age
        self.name = name
        self.__money = 0
        self.__house = None

    def info(self):
        print(f'age --> {self.age}, name --> {self.name}, house --> {self.__house}, '
              f'Остаток денежных средств на вашем счету после покупки дома --> {self.__money}')

    @staticmethod
    def default_info():
        print(f'name --> {Human.default_name}, age --> {Human.default_age}')

    def earn_money(self, amount_money):
        print(f'Сумма на счету ---> {self.__money}')
        self.__money += amount_money
        print(f'Сумма заработка --> {amount_money},конечная сумма на счету'
              f' после зачисления заработка --> 'f'{self.__money}')

    def buy_house(self, house_link, amount_discount):
        price = house_link.final_price(amount_discount)
        if self.__money >= price:
            self.__make_deal(price, house_link)
            print(f'Скидка на дом ----> {amount_discount} %')
            print(f'Поздравляем с успешной покупкой дома ')
        else:
            print(f'Ошибка сделки ----> У вас не хватает денег на покупку этого дома, '
                  f' конечная стоимость дома с вычетом скидки --> {price}')

    def __make_deal(self, prise, house):
        self.__money -= prise
        self.__house = house


class House:

    def __init__(self, _area, _price):
        self._area = _area
        self._price = _price

    def final_price(self, discount):
        final_sum: House = self._price * (100 - discount) / 100
        print(f'Конечная цена дома который вы присмотрели --> {final_sum} '
              f' Cумма скидки --> {self._price  - final_sum} ')
        return final_sum


class SmallHouse(House):
    default_area = 40

    def __init__(self, price):
        super().__init__(SmallHouse.default_area, price)