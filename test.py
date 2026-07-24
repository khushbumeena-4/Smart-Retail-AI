from database import *

create_table()

products = get_all_products()

for product in products:
    print(product)