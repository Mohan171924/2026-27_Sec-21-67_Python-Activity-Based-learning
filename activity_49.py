products = [
    ("Pen", 10, 20),
    ("Book", 50, 15),
    ("Pencil", 5, 30)
]

for name, price, quantity in products:
    value = price * quantity
    print(name, "Value:", value)