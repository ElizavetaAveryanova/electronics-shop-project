import csv
class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    def __repr__(self) -> str:
        """
        Возвращает информацию об объекте: название класса(атрибуты экземпляра)
        """
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self) -> str:
        """
        Возвращает информацию об объекте: название товара
        """
        return self.__name

    @property
    def name(self) -> str:
        """
        Возвращает название товара
        """
        return self.__name

    @name.setter
    def name(self, new_name: str) -> None:
        """
        Присваивает атрибуту name значение new_name,
        при условии, что длина названия товара не больше 10 символов
        """
        if len(new_name) <= 10:
            self.__name = new_name
        else:
            self.__name = new_name[:10]

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        total_price = self.price * self.quantity
        return total_price

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate
        return None

    @classmethod
    def instantiate_from_csv(cls, csvfile):
        """
        Инициализирует экземпляры класса Item данными из файла src/items.csv
        """
        cls.all.clear()

        with open(csvfile, newline='', encoding="windows-1251") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                cls(row['name'], float(row['price']), int(row['quantity']))

    @staticmethod
    def string_to_number(str_number: str) -> int:
        """
        Возвращает число из числа-строки
        """
        return int(float(str_number))

    def __add__(self, other):
        """
        Сложение экземпляров класса Phone и Item (сложение по количеству товара в магазине)
        """
        if isinstance(other, Item):
            return self.quantity + other.quantity
        raise Exception('Недопустимо сложение Phone или Item с экземплярами не Phone или Item классов')

    def __radd__(self, other):
        if isinstance(other, Item):
            return other.quantity + self.quantity
        raise Exception('Недопустимо сложение Phone или Item с экземплярами не Phone или Item классов')
