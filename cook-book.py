import json

def read_cook_book():
    cook_book_file_name = input('Введите название файла, где лежит книга рецептов: ')
    with open(cook_book_file_name, encoding = 'utf_8') as f:
        cook_book = json.load(f)
    return cook_book

def get_shop_list_by_dishes(dishes, person_count, cook_book):
    shop_list = {}
    for dish in dishes:
        for ingridient in cook_book[dish]:
            new_shop_list_item = dict(ingridient)
            new_shop_list_item['quantity'] *= person_count
            if new_shop_list_item['ingridient_name'] not in shop_list:
                shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
            else:
                shop_list[new_shop_list_item['ingridient_name']]['quantity'] += new_shop_list_item['quantity']
    return shop_list

def print_shop_list(shop_list):
    for shop_list_item in shop_list.values():
        print('{ingridient_name} {quantity} {measure}'.format(**shop_list_item))
        
def create_shop_list():
    person_count = int(input('Введите количество человек: '))
    dishes = input('Введите блюда в расчете на одного человека (через запятую): ').lower().split(', ')
    cook_book = read_cook_book()
    shop_list = get_shop_list_by_dishes(dishes, person_count, cook_book)
    print('==================================================')
    print('Список покупок:')
    print_shop_list(shop_list)
    print('==================================================')

create_shop_list()