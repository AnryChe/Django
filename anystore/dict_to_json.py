import json

links_menu = [
    {'href': 'main', 'name': 'домой'},
    {'href': 'products', 'name': 'продукты'},
    {'href': 'contact', 'name': 'контакты'},
]

prod_menu = [
    {'href': 'products_all', 'name': 'все товары'},
    {'href': 'products_home', 'name': 'для дома'},
    {'href': 'products_office', 'name': 'для офиса'},
    {'href': 'products_modern', 'name': 'модерн'},
    {'href': 'products_classic', 'name': 'классика'},
]


def dict_to_json(dict, file_name):
    with open(f'{file_name}.json', 'w', encoding = 'utf-8') as json_file:
        json.dump(dict, json_file)


dict_to_json(links_menu, 'links')
dict_to_json(prod_menu, 'prods')

