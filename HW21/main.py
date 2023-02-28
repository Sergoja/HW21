from request import Request
from store import Store
from shop import Shop

store = Store(
    items={
        "печеньки": 18,
        "собачки": 21,
        "коробки": 15,
        "чипсы": 7,
        "рулеты": 9,
        "сушки": 3,
    }
)

shop = Shop(
    items={
        "печеньки": 3,
        "собачки": 4,
        "коробки": 5,
        "чипсы": 3,
        "рулеты": 2,
    }
)

storages = {
    'магазин': shop,
    'склад': store,
}


def main():
    print('\nДобрый день!\n')

    while True:
        for storage_name in storages:
            print(f'Сейчас в {storage_name}:\n {storages[storage_name].get_items()}')

        user_input = input(
            'Введите запрос в формате "Доставить 3 печеньки из склад в магазин"\n'
            'Введите "стоп" или "stop", если хотите закончить:\n'
        )
        if user_input in ('stop', 'стоп'):
            break

        request = Request(request=user_input, storages=storages)

        from_storage = storages[request.departure].remove(request.product, request.quantity)
        if from_storage in ['Нет такого', 'Не хватает товара']:
            print(f'{from_storage}\nУ курьера возникли трудности')
            pass
        else:
            print(f'Курьер забрал {request.quantity} {request.product} из {request.departure}')
            print(f'Курьер везёт {request.quantity} {request.product} из {request.departure}')
            to_storage = storages[request.destination].add(request.product, request.quantity)
            if to_storage in ['Слишком много разных товаров', 'Нет места']:
                print(f'{to_storage}\nУ курьера возникли трудности, товар возвращен в {request.departure}')
                storages[request.departure].add(request.product, request.quantity)
                pass
            else:
                print(f'{request.quantity} {request.product} доставлен в {request.destination}')


if __name__ == '__main__':
    main()


