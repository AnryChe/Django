from django.shortcuts import render

from dict_from_json import from_json


# links_menu = [
#     {'href': 'main', 'name': 'домой'},
#     {'href': 'products', 'name': 'продукты'},
#     {'href': 'contact', 'name': 'контакты'},
# ]
links_menu = from_json('links.json')              # Так и не заработал сайт с загрузкой из файла.

# prod_menu = [
#     {'href': 'products_all', 'name': 'все товары'},
#     {'href': 'products_home', 'name': 'для дома'},
#     {'href': 'products_office', 'name': 'для офиса'},
#     {'href': 'products_modern', 'name': 'модерн'},
#     {'href': 'products_classic', 'name': 'классика'},
# ]

prod_menu = from_json('prods.json')               # Аналогично

# Create your views here.
def main(request):
    context = {
        'title': 'Главная',
        'links_menu': links_menu
    }
    return render(request, 'mainapp/index.html', context)


def products(request):
    context = {
        'title': 'продукты',
        'links_menu': links_menu,
        'prod_menu':prod_menu,
    }
    return render(request, 'mainapp/products.html', context)


def contact(request):
    context = {
        'title': 'контакты',
        'links_menu': links_menu
    }
    return render(request, 'mainapp/contact.html', context)