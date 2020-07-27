from django.shortcuts import render

links_menu = [
    {'href': 'main', 'name': 'домой'},
    {'href': 'products', 'name': 'продукты'},
    {'href': 'contact', 'name': 'контакты'},
]

# Create your views here.
def main(request):
    return render(request, 'mainapp/index.html', {'links_menu':links_menu})

def products(request):
    return render(request, 'mainapp/products.html', {'links_menu':links_menu})

def contact(request):
    return render(request, 'mainapp/contact.html', {'links_menu':links_menu})