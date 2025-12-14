import os
import django
import random
from django.core.files.base import ContentFile

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from store.models import Category, Product

# Clear existing data
Category.objects.all().delete()
Product.objects.all().delete()

# Create Categories
cats = {
    'elektronika': 'Elektronika',
    'maishiy-texnika': 'Maishiy Texnika',
    'kiyimlar': 'Kiyimlar',
    'poyabzallar': 'Poyabzallar',
    'aksesuarlar': 'Aksesuarlar',
    'gozallik': 'Go\'zallik',
    'sport': 'Sport',
    'uy-rozgor': 'Uy-ro\'zg\'or',
    'kitoblar': 'Kitoblar',
}

category_objs = []
for slug, name in cats.items():
    c = Category.objects.create(name=name, slug=slug)
    category_objs.append(c)

# Create Products
adjectives = ['Yangi', 'Tezkor', 'Zamonaviy', 'Arzon', 'Sifatli', 'Original', 'Zo\'r', 'Katta', 'Kichik']
nouns = ['Telefon', 'Noutbuk', 'Televizor', 'Futbolka', 'Shim', 'Krossovka', 'Sumka', 'Soat', 'Kitob', 'Fen']

def create_products(n=60):
    for i in range(n):
        cat = random.choice(category_objs)
        name = f"{random.choice(adjectives)} {random.choice(nouns)} {i+1}"
        slug = f"product-{i+1}"
        price = random.randint(50, 5000) * 1000
        desc = "Bu mahsulot juda sifatli va hamyonbop. Hozir sotib oling!"
        
        is_hot = random.random() < 0.2  # 20% chance to be hot
        sales_count = random.randint(0, 1000)

        Product.objects.create(
            category=cat,
            name=name,
            slug=slug,
            description=desc,
            price=price,
            stock=random.randint(5, 50),
            is_hot=is_hot,
            sales_count=sales_count
        )
        print(f"Created {name}")

create_products()
print("Database populated with 60+ items.")
