from database import get_product, update_quantity


def generate_bill(cart):

    bill = []
    grand_total = 0

    print("\n" + "=" * 45)
    print("        SMART RETAIL CHECKOUT")
    print("=" * 45)
    print("{:<15}{:<8}{:<10}{:<10}".format(
        "Product", "Qty", "Price", "Total"))
    print("-" * 45)

    for product_name, quantity in cart.items():

        product = get_product(product_name)

        if product is None:
            print(f"{product_name} not found!")
            continue

        _, name, price, stock = product

        if quantity > stock:
            print(f"Only {stock} {name} available.")
            continue

        total = price * quantity
        grand_total += total

        bill.append({
            "name": name,
            "quantity": quantity,
            "price": price,
            "total": total
        })

        update_quantity(name, quantity)

        print("{:<15}{:<8}{:<10}{:<10}".format(
            name,
            quantity,
            price,
            total
        ))

    print("-" * 45)
    print(f"Grand Total : ₹{grand_total}")
    print("=" * 45)

    return bill, grand_total