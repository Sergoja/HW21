from abs_storage import Storage


class Store(Storage):
    def __init__(self, items: dict, capacity: int = 100):
        self.__items = items
        self.__capacity = capacity

    def add(self, name, quantity):
        if self.get_free_space() < quantity:
            return 'Нет места'

        if name in self.__items:
            self.__items[name] += quantity
        else:
            self.__items[name] = quantity

    def remove(self, name, quantity):
        if name not in self.__items:
            return 'Нет такого'

        if self.__items[name] < quantity:
            return 'Не хватает товара'

        self.__items[name] -= quantity

        if self.__items[name] == 0:
            self.__items.pop(name)

    def get_free_space(self):
        return self.__capacity - sum(self.__items.values())

    def get_items(self):
        return self.__items
